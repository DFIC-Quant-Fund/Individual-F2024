**DFIC Quant Team – Individual Project Proposal**

**Overview**

**Note: Kalman Filter was changed to moving average for this project.**

The project will implement the Kalman Filter to estimate the moving average of a stock’s price. The strategy involves entering long or short positions based on the z-score, which measures how far the current price is from the Kalman filter in terms of standard deviation. The strategy will be to,

1. **Long Entry**: Enter a long position when the z-score is below a certain threshold.
2. **Short Entry**: Enter a short position when the z-score is above a certain threshold.
3. **Exit Long**: Exit a long position when the z-score reverts to a higher threshold.
4. **Exit Short**: Exit a short position when the z-score reverts to a lower threshold.
5. **Stop-Loss**: Exit the position if the price moves beyond a specified percentage from the entry price. This is to limit risk in case of abnormal events.

The z score can be defined as:

- X is the current price.
- μ is the moving average price given by the Kalman Filter.
- is the standard deviation of stock.

**Hypothesis**

The hypothesis behind this strategy is that stock prices exhibit short-term noise around a longer-term trend, which can be captured using the Kalman Filter. By calculating the z-score (the deviation of the current price from the estimated trend in terms of standard deviations), we can identify profitable entry and exit points:

A low z-score indicates that the stock is trading significantly below its estimated trend, suggesting a potential buying opportunity.

A high z-score indicates that the stock is trading significantly above its estimated trend, suggesting a potential selling opportunity.

**Resources**

- Python
- QuantConnect
- Libraries: Pandas, Matplotlib for data manipulation and visualization
- yfinance for retrieving historical stock price data
- Kalman filter implementation (pykalman)

**Timeline**

Week 1: Research & Setup

- Review literature on Kalman Filters in finance.
- Set up the development environment (Python, yfinance, pykalman).
- Get historical data

Week 2: Initial Implementation

- Implement the Kalman Filter to estimate the moving average.
- Compute the z-score based on the stock’s price and moving average.
- Define basic entry and exit rules for long and short positions.

Week 3: Backtesting & Optimization

- Conduct backtesting of the strategy using historical data.
- Optimize parameters (e.g., z-score thresholds, stop-loss percentage).
- Analyze performance metrics such as Sharpe ratio and max drawdown.

Week 4: Refinement & Finalization

- Refine the strategy based on backtesting results.
- Finalize stop-loss mechanisms and risk management strategies.
- Prepare performance visualization and trading signals.
