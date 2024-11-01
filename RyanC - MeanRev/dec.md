**DFIC Quant Team – Individual Project Proposal**

**Overview**

This project aims to implement a mean reversion trading strategy that adjusts for market volatility, focusing on the S&P 500 index. The underlying principle is that stock prices will revert to their mean, but this reversion can be influenced by the prevailing market volatility. Using Quantconnect, the algorithm will use moving averages to identify optimal entry and exit points.

**Hypothesis**

The hypothesis is that stocks temporarily deviating from their mean price offer trading opportunities, and these opportunities become more appealing by adjusting for market volatility. A 50-day EMA will be used to track more immediate price trends, allowing the algorithm to respond quickly to recent price deviations. A 200-day SMA will be employed to provide a stable baseline for the mean, balancing sensitivity in identifying mean reversion opportunities. These moving averages will be utilized to generate buy or sell signals. The strategy will aim to capitalize on mean reversion.

**Buy Signals:**

- Price falls significantly below the 50-day EMA
- Price is below the 200-day SMA

**Sell Signals:**

- Price rises significantly above the 50-day EMA
- Price is above the 200-day SMA

**Resources**

**QuantConnect Data Library:** Access to historical price data and fundamental data for S&P 500 equities.

**Python Libraries:** Pandas, yfinance and NumPy which are essential for data manipulation and moving averages
