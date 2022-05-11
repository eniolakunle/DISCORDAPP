class TDEndpointData:
    GET_ACCOUNTS = "https://api.tdameritrade.com/v1/accounts/{accountID}"
    GET_TOKEN = "https://api.tdameritrade.com/v1/oauth2/token"
    GET_QUOTE = "https://api.tdameritrade.com/v1/marketdata/{symbol}/quotes"
    PLACE_ORDER = "https://api.tdameritrade.com/v1/accounts/{accountID}/orders"
    GET_TRANSACTIONS = (
        "https://api.tdameritrade.com/v1/accounts/{accountID}/transactions"
    )

    TD_TOKEN = {
        "refresh_token": "hKY9X/QGcmmS2VnVP0FmZkrXMhp58At7X9ME8iw9ilVc/sh1PJ2M0/fmXawMqTA4sKNvTqBZU9Wl+H9iU6w+/79dowwpDDfgZUkzx/+WUYHWaJ6853Wz9E1MpYsgOR8VhsiomkFb9Yw9vPNJfGul3AixQtQVCHRMQRNXGGDS+EQaTeHSJANPpMQMHi8C5cIp4R788rAVmI+0LNQwa8XdtF+0j8YYhdEYUMNNR6i69aK4B3xZvybxIptReo7mzpTS1IZiagjUuHi5lYFBVissfnLjVYBQdfzHwklXzDbVlPp+/PCcPDCB/V9HagTMatJsJfGbXPKu7osHNnXON/wnWNx4B65BKbjO9CHNNq4pRI8pNXpZxAUSwp6sR5h4oD6m70KarrgaUQlR/dvCCBu8kJA013A+3BBG+3oIJOfvyWgJg24Tr/p1TVHPkv+100MQuG4LYrgoVi/JHHvlC3i9vTjsqQ48N9Z+SixwiLd6/xy96KebCRqCgu3li8Agt5lX12Tahp689cVeCzB55iJpp1vtQvAkSxMw9TvCjbOvPmfYsQwXneqbZUbrZmDt+1mc1Ohk7gSQ0Z0wj9w6rW40R1T9WcVp0rQPEYxbjyRs8cLnlVihH9l5haoiTgY9JBeZHmlpZe4B928crqqdzoxdst1j9t5cfhUi0vXRoA95KcH+Z86GtwYiqjRVAiRHdtMBhL+q2plEPibvzTWJt8f9RNZ3IZGgY3NjOv+hhrXfbzJ+9Y9bzEW1XGyMgg917ON6xkTthIMYbgyAYMY/YuCKIZIo2Oigh6v3sBg8pTurDN62IoRg390it4M2AKekXD7ZaDvtFjd3WzuAuG1ouEHD+Acy04TmaIgqmOTZmD0TvBkWRp177NqbyTw4KhmujZl0Ce2yU0PuyCU=212FD3x19z9sWBHDJACbC00B75E",
    }
    BUY_OPTION_BODY = {
        "complexOrderStrategyType": "NONE",
        "orderType": "MARKET",
        "session": "NORMAL",
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegCollection": [
            {
                "instruction": "BUY_TO_OPEN",  # "SELL_TO_CLOSE",
                "quantity": 1,
                "instrument": {
                    "symbol": "",  # XYZ_032015C49
                    "assetType": "OPTION",
                },
            }
        ],
    }


# //CashAccount:
# {
#   "type": "'CASH' or 'MARGIN'",
#   "accountId": "string",
#   "roundTrips": 0,
#   "isDayTrader": false,
#   "isClosingOnlyRestricted": false,
#   "positions": [
#     {
#       "shortQuantity": 0,
#       "averagePrice": 0,
#       "currentDayProfitLoss": 0,
#       "currentDayProfitLossPercentage": 0,
#       "longQuantity": 0,
#       "settledLongQuantity": 0,
#       "settledShortQuantity": 0,
#       "agedQuantity": 0,
#       "instrument": "\"The type <Instrument> has the following subclasses [Equity, FixedIncome, MutualFund, CashEquivalent, Option] descriptions are listed below\"",
#       "marketValue": 0
#     }
#   ],
#   "orderStrategies": [
#     {
#       "session": "'NORMAL' or 'AM' or 'PM' or 'SEAMLESS'",
#       "duration": "'DAY' or 'GOOD_TILL_CANCEL' or 'FILL_OR_KILL'",
#       "orderType": "'MARKET' or 'LIMIT' or 'STOP' or 'STOP_LIMIT' or 'TRAILING_STOP' or 'MARKET_ON_CLOSE' or 'EXERCISE' or 'TRAILING_STOP_LIMIT' or 'NET_DEBIT' or 'NET_CREDIT' or 'NET_ZERO'",
#       "cancelTime": {
#         "date": "string",
#         "shortFormat": false
#       },
#       "complexOrderStrategyType": "'NONE' or 'COVERED' or 'VERTICAL' or 'BACK_RATIO' or 'CALENDAR' or 'DIAGONAL' or 'STRADDLE' or 'STRANGLE' or 'COLLAR_SYNTHETIC' or 'BUTTERFLY' or 'CONDOR' or 'IRON_CONDOR' or 'VERTICAL_ROLL' or 'COLLAR_WITH_STOCK' or 'DOUBLE_DIAGONAL' or 'UNBALANCED_BUTTERFLY' or 'UNBALANCED_CONDOR' or 'UNBALANCED_IRON_CONDOR' or 'UNBALANCED_VERTICAL_ROLL' or 'CUSTOM'",
#       "quantity": 0,
#       "filledQuantity": 0,
#       "remainingQuantity": 0,
#       "requestedDestination": "'INET' or 'ECN_ARCA' or 'CBOE' or 'AMEX' or 'PHLX' or 'ISE' or 'BOX' or 'NYSE' or 'NASDAQ' or 'BATS' or 'C2' or 'AUTO'",
#       "destinationLinkName": "string",
#       "releaseTime": "string",
#       "stopPrice": 0,
#       "stopPriceLinkBasis": "'MANUAL' or 'BASE' or 'TRIGGER' or 'LAST' or 'BID' or 'ASK' or 'ASK_BID' or 'MARK' or 'AVERAGE'",
#       "stopPriceLinkType": "'VALUE' or 'PERCENT' or 'TICK'",
#       "stopPriceOffset": 0,
#       "stopType": "'STANDARD' or 'BID' or 'ASK' or 'LAST' or 'MARK'",
#       "priceLinkBasis": "'MANUAL' or 'BASE' or 'TRIGGER' or 'LAST' or 'BID' or 'ASK' or 'ASK_BID' or 'MARK' or 'AVERAGE'",
#       "priceLinkType": "'VALUE' or 'PERCENT' or 'TICK'",
#       "price": 0,
#       "taxLotMethod": "'FIFO' or 'LIFO' or 'HIGH_COST' or 'LOW_COST' or 'AVERAGE_COST' or 'SPECIFIC_LOT'",
#       "orderLegCollection": [
#         {
#           "orderLegType": "'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'",
#           "legId": 0,
#           "instrument": "\"The type <Instrument> has the following subclasses [Equity, FixedIncome, MutualFund, CashEquivalent, Option] descriptions are listed below\"",
#           "instruction": "'BUY' or 'SELL' or 'BUY_TO_COVER' or 'SELL_SHORT' or 'BUY_TO_OPEN' or 'BUY_TO_CLOSE' or 'SELL_TO_OPEN' or 'SELL_TO_CLOSE' or 'EXCHANGE'",
#           "positionEffect": "'OPENING' or 'CLOSING' or 'AUTOMATIC'",
#           "quantity": 0,
#           "quantityType": "'ALL_SHARES' or 'DOLLARS' or 'SHARES'"
#         }
#       ],
#       "activationPrice": 0,
#       "specialInstruction": "'ALL_OR_NONE' or 'DO_NOT_REDUCE' or 'ALL_OR_NONE_DO_NOT_REDUCE'",
#       "orderStrategyType": "'SINGLE' or 'OCO' or 'TRIGGER'",
#       "orderId": 0,
#       "cancelable": false,
#       "editable": false,
#       "status": "'AWAITING_PARENT_ORDER' or 'AWAITING_CONDITION' or 'AWAITING_MANUAL_REVIEW' or 'ACCEPTED' or 'AWAITING_UR_OUT' or 'PENDING_ACTIVATION' or 'QUEUED' or 'WORKING' or 'REJECTED' or 'PENDING_CANCEL' or 'CANCELED' or 'PENDING_REPLACE' or 'REPLACED' or 'FILLED' or 'EXPIRED'",
#       "enteredTime": "string",
#       "closeTime": "string",
#       "tag": "string",
#       "accountId": 0,
#       "orderActivityCollection": [
#         "\"The type <OrderActivity> has the following subclasses [Execution] descriptions are listed below\""
#       ],
#       "replacingOrderCollection": [
#         {}
#       ],
#       "childOrderStrategies": [
#         {}
#       ],
#       "statusDescription": "string"
#     }
#   ],
#   "initialBalances": {
#     "accruedInterest": 0,
#     "cashAvailableForTrading": 0,
#     "cashAvailableForWithdrawal": 0,
#     "cashBalance": 0,
#     "bondValue": 0,
#     "cashReceipts": 0,
#     "liquidationValue": 0,
#     "longOptionMarketValue": 0,
#     "longStockValue": 0,
#     "moneyMarketFund": 0,
#     "mutualFundValue": 0,
#     "shortOptionMarketValue": 0,
#     "shortStockValue": 0,
#     "isInCall": false,
#     "unsettledCash": 0,
#     "cashDebitCallValue": 0,
#     "pendingDeposits": 0,
#     "accountValue": 0
#   },
#   "currentBalances": {
#     "accruedInterest": 0,
#     "cashBalance": 0,
#     "cashReceipts": 0,
#     "longOptionMarketValue": 0,
#     "liquidationValue": 0,
#     "longMarketValue": 0,
#     "moneyMarketFund": 0,
#     "savings": 0,
#     "shortMarketValue": 0,
#     "pendingDeposits": 0,
#     "cashAvailableForTrading": 0,
#     "cashAvailableForWithdrawal": 0,
#     "cashCall": 0,
#     "longNonMarginableMarketValue": 0,
#     "totalCash": 0,
#     "shortOptionMarketValue": 0,
#     "mutualFundValue": 0,
#     "bondValue": 0,
#     "cashDebitCallValue": 0,
#     "unsettledCash": 0
#   },
#   "projectedBalances": {
#     "accruedInterest": 0,
#     "cashBalance": 0,
#     "cashReceipts": 0,
#     "longOptionMarketValue": 0,
#     "liquidationValue": 0,
#     "longMarketValue": 0,
#     "moneyMarketFund": 0,
#     "savings": 0,
#     "shortMarketValue": 0,
#     "pendingDeposits": 0,
#     "cashAvailableForTrading": 0,
#     "cashAvailableForWithdrawal": 0,
#     "cashCall": 0,
#     "longNonMarginableMarketValue": 0,
#     "totalCash": 0,
#     "shortOptionMarketValue": 0,
#     "mutualFundValue": 0,
#     "bondValue": 0,
#     "cashDebitCallValue": 0,
#     "unsettledCash": 0
#   }
# }
