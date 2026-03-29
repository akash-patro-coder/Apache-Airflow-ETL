import pandas as pd

def transform_market_data(polygon_response, ds):
    columns = {
        "status": None,
        "from": ds,
        "symbol": "AMZN",
        "open": None,
        "high": None,
        "low": None,
        "close": None,
        "volume": None
    }

    flattened_record = []
    for key, default in columns.items():
        flattened_record.append(polygon_response.get(key, default))

    df = pd.DataFrame([flattened_record], columns=columns.keys())
    return df