from AlgorithmImports import *
import numpy as np

class Kalman_ZScore(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2010, 1, 1)
        self.SetEndDate(2018, 1, 1)
        self.SetCash(100000)

        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.benchmark_symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.SetBenchmark(self.benchmark_symbol)

        self.lookback = 100 
        self.stop_loss_pct = 0.07 

        self.sma = self.SMA(self.symbol, self.lookback, Resolution.Daily)

        self.SetWarmUp(self.lookback)

        self.price_window = RollingWindow[float](self.lookback)

        self.z_threshold_long = 2  
        self.z_threshold_short = -2  
        self.exit_threshold_long = -0.75  
        self.exit_threshold_short = 0.75  
        self.entry_price = None

    def OnData(self, data):
        if not data.ContainsKey(self.symbol) or data[self.symbol] is None:
            return

        price = data[self.symbol].Close
        self.price_window.Add(price) 

        if self.sma.IsReady and self.price_window.Count == self.lookback:
            mu = self.sma.Current.Value 
            sigma = np.std([x for x in self.price_window]) 

            z_score = (price - mu) / sigma if sigma != 0 else 0 

            self.Log(f"Current Price (C): {price}, Mean (μ): {mu}, Std Dev (σ): {sigma}")

            # Long entry
            if z_score < self.z_threshold_long and not self.Portfolio.Invested:
                self.SetHoldings(self.symbol, 1)  # Buy full position
                self.entry_price = price
                self.Log(f"Entering long position at {price} with Z-Score: {z_score}")

            # Short entry
            elif z_score > self.z_threshold_short and not self.Portfolio.Invested:
                self.SetHoldings(self.symbol, -1)  # Short full position
                self.entry_price = price
                self.Log(f"Entering short position at {price} with Z-Score: {z_score}")

            # Exit long
            elif z_score > self.exit_threshold_long and self.Portfolio[self.symbol].IsLong:
                self.Liquidate(self.symbol)
                self.Log(f"Exiting long position at {price} with Z-Score: {z_score}")

            # Exit short
            elif z_score < self.exit_threshold_short and self.Portfolio[self.symbol].IsShort:
                self.Liquidate(self.symbol)
                self.Log(f"Exiting short position at {price} with Z-Score: {z_score}")

            # Stop-Loss
            if self.Portfolio.Invested and self.entry_price is not None:
                if self.Portfolio[self.symbol].IsLong and price < self.entry_price * (1 - self.stop_loss_pct):
                    self.Liquidate(self.symbol)
                    self.Log(f"Long stop-loss triggered at {price}")

                elif self.Portfolio[self.symbol].IsShort and price > self.entry_price * (1 + self.stop_loss_pct):
                    self.Liquidate(self.symbol)
                    self.Log(f"Short stop-loss triggered at {price}")
