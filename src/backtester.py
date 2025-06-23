def simple_signal_backtest(df, signal_col="signal", holding_period=5, cost_per_trade=0.0):
    import numpy as np
    df = df.copy()

    # Appliquer uniquement si position active (1 ou -1)
    df["future_return"] = df["midprice"].shift(-holding_period) - df["midprice"]
    df["position"] = df[signal_col]

    # pnl = position * variation de prix - coût si position != 0
    df["pnl"] = df["position"] * df["future_return"]
    df.loc[df["position"] != 0, "pnl"] -= cost_per_trade

    # Cumuler seulement si position
    df["cum_pnl"] = df["pnl"].cumsum()
    return df

    