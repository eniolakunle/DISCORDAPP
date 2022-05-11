class MockTDClient:
    def __init__(self):
        pass

    def get_positions(self):
        return TD_MOCK_POSITIONS


TD_MOCK_POSITIONS = [
    {
        "shortQuantity": 0.0,
        "averagePrice": 2.42,
        "currentDayCost": 341.0,
        "currentDayProfitLoss": -239.0,
        "currentDayProfitLossPercentage": -70.09,
        "longQuantity": 2.0,
        "settledLongQuantity": 0.0,
        "settledShortQuantity": 0.0,
        "instrument": {
            "assetType": "OPTION",
            "cusip": "0QQQ..PT20317500",
            "symbol": "QQQ_042922P317.5",
            "description": "QQQ Apr 29 2022 317.5 Put",
            "type": "VANILLA",
            "putCall": "PUT",
            "underlyingSymbol": "QQQ",
        },
        "marketValue": 102.0,
        "maintenanceRequirement": 0.0,
        "previousSessionLongQuantity": 0.0,
    },
    {
        "shortQuantity": 0.0,
        "averagePrice": 2.42,
        "currentDayCost": 341.0,
        "currentDayProfitLoss": -239.0,
        "currentDayProfitLossPercentage": -70.09,
        "longQuantity": 2.0,
        "settledLongQuantity": 0.0,
        "settledShortQuantity": 0.0,
        "instrument": {
            "assetType": "OPTION",
            "cusip": "0QQQ..PT20317500",
            "symbol": "TTD_042922P317.5",
            "description": "QQQ Apr 29 2022 317.5 Put",
            "type": "VANILLA",
            "putCall": "PUT",
            "underlyingSymbol": "QQQ",
        },
        "marketValue": 102.0,
        "maintenanceRequirement": 0.0,
        "previousSessionLongQuantity": 0.0,
    },
    {
        "shortQuantity": 0.0,
        "averagePrice": 2.42,
        "currentDayCost": 341.0,
        "currentDayProfitLoss": -239.0,
        "currentDayProfitLossPercentage": -70.09,
        "longQuantity": 2.0,
        "settledLongQuantity": 0.0,
        "settledShortQuantity": 0.0,
        "instrument": {
            "assetType": "OPTION",
            "cusip": "0QQQ..PT20317500",
            "symbol": "DDOG_042922P317.5",
            "description": "QQQ Apr 29 2022 317.5 Put",
            "type": "VANILLA",
            "putCall": "PUT",
            "underlyingSymbol": "QQQ",
        },
        "marketValue": 102.0,
        "maintenanceRequirement": 0.0,
        "previousSessionLongQuantity": 0.0,
    },
    {
        "shortQuantity": 0.0,
        "averagePrice": 2.42,
        "currentDayCost": 341.0,
        "currentDayProfitLoss": -239.0,
        "currentDayProfitLossPercentage": -70.09,
        "longQuantity": 2.0,
        "settledLongQuantity": 0.0,
        "settledShortQuantity": 0.0,
        "instrument": {
            "assetType": "OPTION",
            "cusip": "0QQQ..PT20317500",
            "symbol": "QQQ_042922C317.5",
            "description": "QQQ Apr 29 2022 317.5 Put",
            "type": "VANILLA",
            "putCall": "CALL",
            "underlyingSymbol": "QQQ",
        },
        "marketValue": 102.0,
        "maintenanceRequirement": 0.0,
        "previousSessionLongQuantity": 0.0,
    },
    {
        "shortQuantity": 0.0,
        "averagePrice": 2.42,
        "currentDayCost": 341.0,
        "currentDayProfitLoss": -239.0,
        "currentDayProfitLossPercentage": -70.09,
        "longQuantity": 2.0,
        "settledLongQuantity": 0.0,
        "settledShortQuantity": 0.0,
        "instrument": {
            "assetType": "OPTION",
            "cusip": "0QQQ..PT20317500",
            "symbol": "TSLA_042922C317.5",
            "description": "QQQ Apr 29 2022 317.5 Put",
            "type": "VANILLA",
            "putCall": "PUT",
            "underlyingSymbol": "QQQ",
        },
        "marketValue": 102.0,
        "maintenanceRequirement": 0.0,
        "previousSessionLongQuantity": 0.0,
    },
    {
        "shortQuantity": 0.0,
        "averagePrice": 2.42,
        "currentDayCost": 341.0,
        "currentDayProfitLoss": -239.0,
        "currentDayProfitLossPercentage": -70.09,
        "longQuantity": 2.0,
        "settledLongQuantity": 0.0,
        "settledShortQuantity": 0.0,
        "instrument": {
            "assetType": "OPTION",
            "cusip": "0QQQ..PT20317500",
            "symbol": "MSFT_042922P317.5",
            "description": "QQQ Apr 29 2022 317.5 Put",
            "type": "VANILLA",
            "putCall": "PUT",
            "underlyingSymbol": "QQQ",
        },
        "marketValue": 102.0,
        "maintenanceRequirement": 0.0,
        "previousSessionLongQuantity": 0.0,
    },
]
