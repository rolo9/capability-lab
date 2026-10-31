import pandas as pd


def calculate_rolling_average(series: pd.Series, window: int = 3) -> pd.Series:
    """指定した行数の移動平均を計算する。"""
    return series.rolling(window=window).mean()
