from AlgorithmImports import *

class MeanReversion(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 1, 1)  # Start date for backtesting
        self.SetEndDate(2023, 12, 31)    # End date for backtesting
        self.SetCash(100000)           # Starting cash for the backtest
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol  # Add S&P 500 ETF

        # Moving averages
        self.ema50 = self.EMA(self.spy, 50, Resolution.Daily)
        self.sma200 = self.SMA(self.spy, 200, Resolution.Daily)

        self.lookback = 1  # Lookback to prevent rebuying or reselling immediately
        self.lastAction = self.Time  # Track the time of the last trade

    def OnData(self, data: Slice):
        if not (self.ema50.IsReady and self.sma200.IsReady): # Check if there's enough data for the moving averages
            return

        price = self.Securities[self.spy].Price
        time_since_last_action = (self.Time - self.lastAction).days

        # Buy conditions: Buy when price drops significantly below 50 day ema and is below 200 day sma
        if price < self.ema50.Current.Value * 0.98 and price < self.sma200.Current.Value: 
            if time_since_last_action >= self.lookback:
                self.SetHoldings(self.spy, 1)
                self.lastAction = self.Time
                self.log("Buying SPY at " + str(price))

        # Sell conditions: Sell when price is significantly above 50 day ema and is above 200 day sma
        elif price > self.ema50.Current.Value * 1.02 and price > self.sma200.Current.Value:
            if time_since_last_action >= self.lookback:
                self.Liquidate(self.spy)
                self.lastAction = self.Time
                self.log(f"Selling SPY at " + str(price))
