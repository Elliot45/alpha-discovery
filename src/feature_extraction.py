def compute_midprice(df):
    df["midprice"] = (df["ask1"] + df["bid1"]) / 2
    return df

def compute_order_imbalance(df):
    df["ofi"] = (df["bid_size1"] - df["ask_size1"]) / (df["bid_size1"] + df["ask_size1"] + 1e-9)
    return df

