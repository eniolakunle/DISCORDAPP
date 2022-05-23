import unittest
from datetime import datetime
from unittest.mock import patch
from parameterized import parameterized
from .clients.test_td_client import MockTDClient
from discord_text_parser import DiscordParser, ParseException


class DiscordParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.discord_parser = DiscordParser()
        return super().setUp()

    @parameterized.expand(
        [
            ("     SLGOAGdfhwloshdslfjodosjhsdhs", "slgoagdfhwloshdslfjodosjhsdhs"),
            (" egfgegweg egweeSSGODSGSOGS", "egfgegweg egweessgodsgsogs"),
            ("31241SFSGSGdhasgasLLL", "31241sfsgsgdhasgaslll"),
            ("bought $amd apr 29 $89 puts @ 1.83", "bought $amd apr 29 $89 puts"),
            (
                "bought $amd apr 29 $89 puts @ 583 Chikcne",
                "bought $amd apr 29 $89 puts",
            ),
            ("bought $aemd apr 29 $81 calls @ 133.83", "bought $aemd apr 29 $81 calls"),
            (
                "couldn't  sit out with the breakout after consolidation                                                                          @stocks investor bought $qqq may 6 $325 calls @3.59. risky play in chop",
                "bought $qqq may 6 $325 calls",
            ),
        ]
    )
    def testCleanString(self, input, expected_output):
        output = self.discord_parser._clean_string(input)
        self.assertEqual(expected_output, output)

    @parameterized.expand(
        [
            (
                [
                    "mar",
                    "18",
                ],
                datetime(1990, 3, 18),
            ),
            (
                [
                    "aug",
                    "18",
                ],
                datetime(1990, 8, 18),
            ),
            (
                [
                    "dec",
                    "1",
                ],
                datetime(1990, 12, 1),
            ),
            (
                [
                    "may",
                    "18",
                ],
                datetime(1990, 5, 18),
            ),
        ]
    )
    def testParseDate(self, input, expected_date):
        output = self.discord_parser._parse_date(input)
        self.assertEqual(output.month, expected_date.month)
        self.assertEqual(output.day, expected_date.day)

    @parameterized.expand(
        [
            ("195.5", 195.5),
            ("195", 195),
            ("200", 200),
            ("1.5", 1.5),
        ]
    )
    def testParsePrice(self, input, expected_output):
        output = self.discord_parser._parse_price(input)
        self.assertEqual(output, expected_output)

    @parameterized.expand(
        [
            (datetime(1990, 2, 1), "23"),
            (datetime(2002, 3, 1), "23"),
            (datetime(2041, 5, 1), "23"),
            (datetime(2001, 7, 1), "22"),
            (datetime(2022, 8, 1), "22"),
            (datetime(2012, 1, 1), "23"),
            (datetime(1997, 4, 1), "23"),
            (datetime(1000, 9, 1), "22"),
            (datetime(2000, 12, 1), "22"),
            (datetime(2099, 11, 1), "22"),
            (datetime(1950, 10, 1), "22"),
            (datetime(2212, 8, 1), "22"),
            (datetime(2021, 6, 1), "23"),
            (datetime(2020, 6, 2), "22"),
        ]
    )
    @patch("discord_text_parser.datetime", wraps=datetime)
    def testGetYear(self, input_date, expected_year, mock_datetime):
        mock_datetime.today.return_value = datetime(2022, 6, 2)
        output = self.discord_parser._get_year(input_date)
        self.assertEqual(expected_year, output)

    @parameterized.expand(
        [
            ("bought $rblx mar 18 $39 puts", ("RBLX_031823P39", 1)),
            ("bought $rblx mar 18 39 puts", ("RBLX_031823P39", 1)),
            ("bought $se Apr 29 $84 put ", ("SE_042923P84", 1)),
        ]
    )
    @patch("discord_text_parser.datetime", wraps=datetime)
    def testRunChecks(self, input, expected_output, mock_datetime):
        mock_datetime.today.return_value = datetime(2022, 6, 1)
        output = self.discord_parser.run_checks(input)
        self.assertEqual(output, expected_output)

    @parameterized.expand(
        [
            "bought mar 18 $39 puts",
            "bought $rblx 18 $39 puts",
            "bought $rblx mar $39 puts",
            "bought $rblx mar 18 puts",
            "bought $rblx mar 18 $39",
            "chicken bought $adbe may 6 $380 puts",
            "344  bought $qqq Apr 29 $325 puts",
            "boug  saht $roku Apr 29 $92 puts",
            "clost ddog @ 7.55 for 13% gains",
            " xited Ttd at 3.09 for 7% gains",
            "of QQQ puts at 3.98 for 14% gains",
        ]
    )
    def testRunChecksExpectedRaise(self, input):
        errors = [
            "does not match format",
            "Malformed discord text",
            "What da heck u send me",
        ]
        with self.assertRaises(ParseException) as exec:
            self.discord_parser.run_checks(input)
        self.assertTrue(any(error in str(exec.exception) for error in errors))

    @parameterized.expand(
        [
            ("bought $adbe may 6 $380 puts", "ADBE_050623P380"),
            ("bought $qqq Apr 29 $325 puts", "QQQ_042923P325"),
            ("bought $roku Apr 29 $92 puts", "ROKU_042923P92"),
            ("bought $se Apr 29 $84 put ", "SE_042923P84"),
            (" bought $iwm Apr 29 $195 put", "IWM_042923P195"),
            ("bought $qqq Apr 29 $330 puts", "QQQ_042923P330"),
            ("bought $nvda Apr 29 $200 call", "NVDA_042923C200"),
            ("Bought shop Aug 13 $1560 call", "SHOP_081322C1560"),
            ("Bought spy Aug 9 441 calls", "SPY_080922C441"),
            ("Bought spy Aug 28 41 calls", "SPY_082822C41"),
            ("Bought $qqq Sep 17 $378 puts", "QQQ_091722P378"),
            ("Bought $snap sep 17 $73.5 puts", "SNAP_091722P73.5"),
            ("Bought $mu Oct 1 $74 calls", "MU_100122C74"),
            ("Bought $tsla Oct 1 $775 call", "TSLA_100122C775"),
            ("Bought $cper Nov 19 $27 calls", "CPER_111922C27"),
            ("Bought $aapl Oct 22 $143 calls", "AAPL_102222C143"),
            ("Bought $aapl Nov 12 $152.5 calls ", "AAPL_111222C152.5"),
            ("Bought $xle Nov 19 $58 calls ", "XLE_111922C58"),
            ("Bought $fas dec 3 $147 calls ", "FAS_120322C147"),
            ("Bought $snow Nov 19 $395 puts ", "SNOW_111922P395"),
            ("Bought $ttd dec 3 $107 calls ", "TTD_120322C107"),
            ("Bought $cdns Dec 17 $185 calls ", "CDNS_121722C185"),
            ("Bought $fb Jan 14 $335 calls ", "FB_011423C335"),
            ("Bought $aapl Jan 7 $180 calls", "AAPL_010723C180"),
            ("Bought $spy Dec 10 469 calls", "SPY_121022C469"),
            ("Bought $mo Feb 4 $51 calls ", "MO_020423C51"),
            ("Bought $pep Feb 4 $172.5 calls", "PEP_020423C172.5"),
            ("Bought $aapl Feb 4 $175 calls ", "AAPL_020423C175"),
            ("bought $amd mar 11 $120 call ", "AMD_031123C120"),
            ("bought $rblx mar 18 $39 puts ", "RBLX_031823P39"),
            ("bought $amd Apr 29 $89 puts @ 1.83", "AMD_042923P89"),
            ("bought $qqq Apr 29 $335 puts @ 3.84", "QQQ_042923P335"),
            ("bought $chwy may 6 $35 puts @ 1.22", "CHWY_050623P35"),
            ("bought $chwy jul 6 $35 puts @ 1.22", "CHWY_070622P35"),
            ("bought $zm Feb 25 $138 put at 4.38", "ZM_022523P138"),
            (
                "bought $arkk may 13 $43 puts @ 0.64",
                "ARKK_051323P43",
            ),
            (
                """Couldn't sit out with the breakout after consolidation

@Stocks investor Bought $qqq may 6 $325 calls @3.59. risky play in chop""",
                "QQQ_050623C325",
            ),
        ]
    )
    @patch("discord_text_parser.TDClient", new=MockTDClient)
    @patch("discord_text_parser.datetime", wraps=datetime)
    def testParse(self, input, expected_output, mock_datetime):
        mock_datetime.today.return_value = datetime(2022, 6, 1)

        output = self.discord_parser.parse(input)
        self.assertEqual(output[0], expected_output)
        self.assertEqual(output[1], 1)

    @parameterized.expand(
        [
            ("exited ddog @ 7.55 for 13% gains", "DDOG_042922P317.5"),
            (" exited Ttd at 3.09 for 7% gains", "TTD_042922P317.5"),
            (" out of QQQ puts at 3.98 for 14% gains", "QQQ_042922P317.5"),
            ("exited QQQ calls at 3.38 for 28% gains", "QQQ_042922C317.5"),
            ("out of QQQ calls @ 3.08 for another 28% gains", "QQQ_042922C317.5"),
            ("out of Tsla at 10.30 for 30% gains", "TSLA_042922C317.5"),
            ("exited QQQ puts at 4.10 for 32% gains", "QQQ_042922P317.5"),
        ]
    )
    @patch("discord_text_parser.TDClient", new=MockTDClient)
    @patch("discord_text_parser.datetime", wraps=datetime)
    def testParseSell(self, input, expected_string, mock_datetime):
        mock_datetime.today.return_value = datetime(2022, 6, 1)

        output = self.discord_parser.parse(input)
        self.assertEqual(output[0], expected_string)
        self.assertEqual(output[1], -2)

    @parameterized.expand(
        [
            "exited $msft call @ 4.30 for 3% loss",
            "exited avgo calls @ 6.77 for 18% loss",
            "exited vxx @ 1.52 for 45% gains",
            "exited spy at 2.26 for 28% gains",
            "out of spy calls @ 3.25 for 28% gains",
            " out of Adobe puts at 4.14 for 22% gains",
            "out of Roku puts at 7.04 for 18% gains",
            " closed IWM puts at 3.49 for 45% gains",
        ]
    )
    @patch("discord_text_parser.TDClient", new=MockTDClient)
    @patch("discord_text_parser.datetime", wraps=datetime)
    def testParseExpectedRaise(self, input, mock_datetime):
        mock_datetime.today.return_value = datetime(2022, 6, 1)
        with self.assertRaises(ParseException) as exec:
            self.discord_parser.parse(input)
        self.assertEqual("Couldn't find a matching order to sell", str(exec.exception))


if __name__ == "__main__":
    unittest.main()
