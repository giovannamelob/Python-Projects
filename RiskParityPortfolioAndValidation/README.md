# Risk Parity Portfolio and Walk-Forward Validation

## Project Overview
This project focuses on constructing a risk-parity portfolio with assets such as S&P 500 Futures, 10-year Treasury Futures, Gold Futures, and US Dollar Index Futures. The portfolio is weighted using inverse volatility, where assets with lower volatility are allocated higher weights. Key performance metrics such as Sharpe Ratio, Sortino Ratio, and Calmar Ratio are computed, and cumulative returns are plotted alongside drawdowns.

## Getting Started

### Installation
To run these scripts, you will need to install several Python libraries. The easiest way to install these is by using pip and the requirements file included in this repository:
pip install -r requirements.txt


## Project Details

### 1. Data Retrieval and Preparation
- **Assets**: This project uses historical adjusted closing prices for four assets:
  - S&P 500 Futures (ES=F)
  - 10-Year Treasury Futures (ZN=F)
  - Gold Futures (GC=F)
  - US Dollar Index Futures (DX=F)
- **Resampling**: The data is resampled to monthly frequency, and missing data is forward-filled.

### 2. Volatility and Risk-Parity Weighting
- **Volatility**: Volatility is measured over a 36-month rolling window.
- **Inverse Volatility**: Assets with lower volatility are allocated higher weights based on the inverse of their volatility.
- **Risk-Parity Portfolio**: The portfolio weights are shifted forward by one period to avoid look-ahead bias, ensuring weights for a given period are based on available data from the previous period.

### 3. Performance Metrics
- **Annualized Mean Return**: The average return over the evaluation period, annualized.
- **Annualized Volatility**: The standard deviation of the portfolio returns, annualized.
- **Skewness and Kurtosis**: Measures of the asymmetry and tailedness of the portfolio return distribution, respectively.
- **Drawdowns**: Ongoing drawdowns are calculated from the portfolio’s cumulative returns, with the maximum drawdown being the largest peak-to-trough decline.
- **Ratios**:
  - **Sharpe Ratio**: Risk-adjusted return relative to the volatility of the portfolio.
  - **Sortino Ratio**: Similar to the Sharpe Ratio, but only penalizes downside volatility.
  - **Calmar Ratio**: Annualized return divided by maximum drawdown.

### 4. Visualization
- **Cumulative Returns vs. Drawdown**: The cumulative returns of the risk-parity portfolio are plotted alongside the ongoing drawdowns, with cumulative returns represented in blue and drawdowns shaded in red.

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
- Project Link: https://github.com/giovannamelob/Python-Projects/tree/main/RiskParityPortfolioAndValidation
