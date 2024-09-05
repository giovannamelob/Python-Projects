# Financial Risk Metrics

## Project Overview
This project focuses on calculating risk metrics such as Value at Risk (VaR), Expected Shortfall (ES), and Sharpe Ratios for portfolios consisting of S&P 500 and 10-year Treasury Futures. It also constructs a 60-40 portfolio, computes its risk-return measures, and performs inflation-adjusted analysis using Consumer Price Index (CPI) data. Key visualizations include cumulative returns, drawdowns, and rolling Sharpe Ratios for the portfolio and its assets.

## Getting Started

### Installation
To run these scripts, you will need to install several Python libraries. The easiest way to install these is by using pip and the requirements file included in this repository:
pip install -r requirements.txt

## Project Details

### 1. Data Retrieval and Analysis
- **S&P 500 and 10-Year Treasury Futures**: The project fetches historical adjusted closing prices for both S&P 500 and 10-Year Treasury Futures using the `yfinance` library. 
- **Log Returns**: Calculates daily logarithmic returns for the fetched data and adjusts for the risk-free rate using the 3-month Treasury Bill rate.

### 2. Portfolio Construction
- **60-40 Portfolio**: Constructs a portfolio weighted 60% in S&P 500 Futures and 40% in 10-Year Treasury Futures. Calculates the log returns, cumulative returns, and risk metrics for this portfolio.
- **Risk Metrics**: Computes Value at Risk (VaR), Expected Shortfall (ES), Delta VaR, Delta Stress ES, skewness, kurtosis, and drawdown for both individual assets and the portfolio.
- **Sharpe Ratio**: The Sharpe Ratio is calculated for S&P 500 Futures, 10-year Treasury Futures, and the combined portfolio. 

### 3. Visualization
- **Cumulative Returns and Drawdowns**: Plots the cumulative returns and ongoing drawdowns for S&P 500 Futures, 10-Year Treasury Futures, and the 60-40 portfolio.
- **Rolling Sharpe Ratios**: Displays rolling Sharpe Ratios over 1-year, 5-year, and 10-year windows for the individual assets and the portfolio.
- **Inflation-Adjusted Sharpe Ratio**: The project adjusts the Sharpe Ratio for inflation using the Consumer Price Index (CPI) from FRED.

### 4. Inflation Adjustment
- **Inflation Data**: Fetches CPI data from the Federal Reserve Economic Data (FRED) and calculates the monthly inflation rate. The project resamples this inflation data to daily frequency and computes the inflation-adjusted Sharpe Ratio for the portfolio.

## Contributing
We welcome contributions from the community. Here are some guidelines you should follow:

1. **Fork the Repository**: Create a fork of our repository on your own GitHub account. This allows you to experiment with changes without affecting the original project.
2. **Make Changes**: Make your modifications in your forked repository. Please keep your changes concise and make sure they follow the existing project structure.
3. **Submit a Pull Request**: Once you are ready, submit a pull request to our repository. Include a clear description of the changes and the benefits they provide.

### Pull Request Guidelines
- Ensure that your code is well-documented and adheres to the existing style.
- Update the README.md if necessary.
- Add comments to your code where necessary to explain complex logic.

## License
This project is released under the MIT License. This allows you to use and modify the software freely for personal and commercial purposes under the conditions listed in the LICENSE file in this repository.

## Contact
- Giovanna Melo Benites - melobenitesgiovanna@gmail.com
- Project Link: https://github.com/giovannamelob/Python-Projects/tree/main/RiskMetrics
