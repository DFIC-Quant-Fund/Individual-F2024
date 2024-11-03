# region imports
from AlgorithmImports import *
# endregion
class FormalFluorescentYellowArmadillo(QCAlgorithm):

    def Initialize(self):
        # IPO april 14 2021
        self.SetStartDate(2021, 4, 14)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        #
        coin = self.AddEquity("COIN", Resolution.Daily)
        # self.AddForex, self.AddFuture...
        # default normalization accounts for split and dividends 
        # coin.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.coin = coin.Symbol
        # benchmarker shows large corelation - means bad for bear market
        self.SetBenchmark("COIN")
        # self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        
        # track buying position 
        self.invested = False
        # self.entryPrice = 0
        # self.period = timedelta(31)
        # self.nextEntryTime = self.Time


    def OnData(self, data):
        if not data.Bars.ContainsKey(self.coin):
            return
        
        days_200 = self.History(self.coin, 200, Resolution.Daily)
        days_50 = self.History(self.coin, 50, Resolution.Daily)
        
        # Access the closing prices
        avgClose_200 = days_200['close'].mean()
        avgClose_50 = days_50['close'].mean()

        price = self.Securities[self.coin].Close

        if avgClose_50 > avgClose_200 and not self.invested:
            self.SetHoldings(self.coin, 1)
            self.invested = True
            self.Log("BUY COIN @" + str(price))
        elif avgClose_50 < avgClose_200 and self.invested:
            self.Liquidate()
            self.invested = False
            self.Log("SELL COIN @" + str(price))
        
        # track net profit 
        net_profit = self.Portfolio.TotalPortfolioValue - 100000
        self.Log(f"Current Net Profit: {net_profit}")

        # price = data.Bars[self.coin].Close
        # price = data[self.coin].Close
        # price = self.Securities[self.coin].Close
        
