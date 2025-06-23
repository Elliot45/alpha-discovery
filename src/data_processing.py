def load_orderbook_data(filepath):
    import pandas as pd
    df = pd.read_csv(filepath, parse_dates=["timestamp"])
    df.sort_values("timestamp", inplace=True)
    return df