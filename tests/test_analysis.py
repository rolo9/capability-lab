import unittest

import pandas as pd
from pandas.testing import assert_series_equal

from src.analysis import calculate_rolling_average


class RollingAverageTests(unittest.TestCase):
    def test_default_window_requires_three_observations(self):
        values = pd.Series([100, 200, 300, 400], name="shipment")
        original = values.copy(deep=True)

        result = calculate_rolling_average(values)

        expected = pd.Series(
            [float("nan"), float("nan"), 200.0, 300.0], name="shipment"
        )
        assert_series_equal(result, expected)
        assert_series_equal(values, original)

    def test_different_window_preserves_index_and_name(self):
        index = pd.date_range("2026-01-01", periods=4, freq="MS")
        values = pd.Series([100, 200, 300, 400], index=index, name="shipment")

        result = calculate_rolling_average(values, window=2)

        expected = pd.Series(
            [float("nan"), 150.0, 250.0, 350.0], index=index, name="shipment"
        )
        assert_series_equal(result, expected)

    def test_channel_loading_produces_a_later_low_indicator(self):
        values = pd.Series([100, 100, 100, 300, 0, 0, 100, 100, 100])
        expected = pd.Series([
            float("nan"), float("nan"), 100.0, 500 / 3, 400 / 3,
            100.0, 100 / 3, 200 / 3, 100.0
        ])

        result = calculate_rolling_average(values, window=3)

        assert_series_equal(result, expected, check_exact=False, rtol=1e-12, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
