from datetime import datetime
from typing import Union

from clients.td_client import TDClient

import re


class ParseException(Exception):
    pass


class DiscordParser:
    def _clean_string(self, string: str) -> str:
        string = string.lower()
        if match := re.search(r"bought|exit|out of|close", string):
            if second_match := re.search(r"(at|@)(\d| )", string):
                string = string[match.start() : second_match.start() - 1]

        # expected end format at all times: bought $qqq may 6 $325 calls, out of QQQ puts
        return string.strip()

    def _get_year(self, parsed_date) -> str:
        today = datetime.today()
        curr_year = today.strftime("%y")
        curr_month = today.month
        parsed_month = parsed_date.month

        if (curr_month - parsed_month) < 0:
            return curr_year
        elif curr_month - parsed_month == 0:
            if (today.day - parsed_date.day) <= 0:
                return curr_year

        return str(int(curr_year) + 1)

    def _parse_date(self, date_list: list) -> datetime:
        return datetime.strptime(" ".join(date_list), "%b %d")

    def _parse_price(self, string_price: str) -> Union[int, float]:
        return float(string_price) if ".5" in string_price else int(string_price)

    def _get_sell_helper(self, stock, option_string, index):
        try:
            if "put" in option_string[index] or "call" in option_string[index]:
                option_type = option_string[index]
                return stock + "-" + option_type
        except:
            return stock

    def _clean_stock_symbol(self, string: list, index: int):
        stock = string[index]
        stock = stock.replace("$", "")
        return stock

    def _get_sell_ticker(self, split_string: list) -> str:
        first = split_string[0]
        if any(signal in first for signal in ["exit", "close"]):
            stock_index = 1
        elif "out" in first:
            stock_index = 2
        else:
            raise ParseException("Couldn't parse sell order.")
        stock = self._clean_stock_symbol(split_string, stock_index)
        return self._get_sell_helper(stock, split_string, stock_index + 1)

    def _get_positions_helper(
        self, positions: list, symbol_split: list, run_extra_verify: bool
    ) -> Union[str, tuple]:
        instruments = []
        for position in positions:
            instrument = position.get("instrument")
            instrument["longQuantity"] = position.get("longQuantity")
            instruments.append(instrument)
        matches = [
            instrument
            for instrument in instruments
            if symbol_split[0].upper() in instrument.get("symbol")
        ]
        if matches and run_extra_verify:
            matches = [
                instrument
                for instrument in matches
                if instrument.get("putCall") in symbol_split[1].upper()
            ]
        if len(matches) == 1:
            instrument = matches[0]
            return instrument.get("symbol"), instrument.get("longQuantity")
        raise ParseException("Couldn't find a matching order to sell")

    def _get_option_position(self, option_symbol: str) -> Union[str, tuple]:
        symbol_split = option_symbol.split("-")
        run_extra_verify = True if len(symbol_split) == 2 else False

        try:
            td_client = TDClient()
            positions = td_client.get_positions()
        except Exception as e:
            raise ParseException(str(e))

        if isinstance(positions, list):
            return self._get_positions_helper(positions, symbol_split, run_extra_verify)
        raise ParseException("Yain't got no positions.")

    def _malform_check(self, split_string: list):
        try:
            int(split_string[-3])
        except ValueError:
            raise ParseException(
                "Malformed discord text, needs all essential values for option chain."
            )

    def _build_option_symbol_helper(
        self, underlying: str, parsed_date: datetime, option_strat: list, price
    ) -> str:
        # XYZ_032015C49
        return (
            underlying.upper()
            + "_"
            + parsed_date.strftime("%m%d")
            + self._get_year(parsed_date)
            + option_strat[0].upper()
            + str(price)
        )

    def _build_option_symbol(self, split_string, option_strat):
        string_date = split_string[2:4]
        parsed_date = self._parse_date(string_date)

        if "$" not in split_string[-2]:
            self._malform_check(split_string)

        price = split_string[-2].replace("$", "")
        price = self._parse_price(price)

        underlying = split_string[1].replace("$", "")
        return self._build_option_symbol_helper(
            underlying, parsed_date, option_strat, price
        )

    def run_checks(self, string_to_check: str) -> tuple:
        string_to_check = self._clean_string(string_to_check)

        split_string = string_to_check.split()
        # ['bought', '$rblx', 'mar', '18', '$39', 'puts']

        # buying option
        if "bought" in split_string[0]:
            option_strat = split_string[-1]
            if option_strat in ["call", "calls", "put", "puts"]:
                try:
                    symbol = self._build_option_symbol(split_string, option_strat)
                    return symbol, 1
                except ValueError as e:
                    raise ParseException(f"{e}")
                except ParseException as e:
                    raise

        # selling option
        elif any(x in split_string for x in ["out", "exited", "closed"]):
            option_symbol = self._get_sell_ticker(split_string)
            if option_symbol:
                position, amount = self._get_option_position(option_symbol)
                return position, -amount
        raise ParseException("What da heck u send me")

    def parse(self, string_to_parse: str) -> tuple:
        # Buy position returns str and postive quantity, sell returns string and negative quantity
        valid_string, amount = self.run_checks(string_to_parse)
        return valid_string, amount  # XYZ_032015C49


if __name__ == "__main__":
    parser = DiscordParser()
    symbol = parser.parse("bought $arkk may 13 $43 puts @ 0.64")
    n = 1
