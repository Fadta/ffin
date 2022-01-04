from __future__ import annotations
import pandas as pd
import numpy as np


class PriceSeries(pd.Series):
    @property
    def _constructor(self):
        return PriceSeries

    def sma(self, window: int) -> PriceSeries:
        return self.rolling(window=window).mean()

    def ema(self, window: int) -> PriceSeries:
        return self.ewm(span=window, adjust=False).mean()

    def rsi(self, window: int) -> PriceSeries:
        delta = self.diff()

        up = delta.clip(lower=0)
        down = -1*delta.clip(upper=0)

        ema_up = up.ewm(com=window, adjust=False).mean()
        ema_down = down.ewm(com=window, adjust=False).mean()

        rs = ema_up/ema_down

        rsi = 100 - (100 / (1 + rs))
        return rsi


class OHLCDataFrame(pd.DataFrame):
    @property
    def _constructor(self):
        return OHLCDataFrame

    def __init__(self, df: pd.DataFrame):
        super().__init__(df)

    def __getitem__(self, key):
        elem = super().__getitem__(key)
        if isinstance(elem, pd.Series):
            return PriceSeries(elem)
        else:
            return elem

    def atr(self, window: int) -> PriceSeries:
        high_low = self['High'] - self['Low']
        high_close = np.abs(self['High'] - self['Close'].shift())
        low_close = np.abs(self['Low'] - self['Close'].shift())

        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = np.max(ranges, axis=1)

        atr = true_range.rolling(window=window).sum()/window
        return PriceSeries(atr)
