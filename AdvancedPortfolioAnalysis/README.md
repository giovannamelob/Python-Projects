# Advanced Portfolio Analysis

## Project Overview
This project provides advanced financial data analysis tools focusing on futures such as S&P 500 and 10-Year Treasury Futures, alongside portfolio analysis including a 60-40 stock-bond portfolio. It calculates and visualizes various financial metrics like Sharpe Ratios, cumulative returns, and volatility, and adjusts inflation returns.

## Getting Started

### Prerequisites
- Python 3.6+
- An active internet connection to fetch financial data.

### Installation
To run these scripts, you will need to install several Python libraries. The easiest way to install these is by using pip and the requirements file included in this repository:
pip install -r requirements.txt

## Project Details

### 1. Data Retrieval and Analysis
- **S&P 500 Futures**: Downloads and calculates Sharpe Ratios and rolling Sharpe Ratios.
- **10-Year Treasury Futures**: Calculates Sharpe Ratio and other performance metrics.
- **60-40 Portfolio**: Constructs a portfolio of S&P 500 and Treasury Futures, and calculates risk metrics like Sharpe Ratio, skewness, and kurtosis.

### 2. Visualization
- **Return Distributions**: Histograms and rolling Sharpe Ratios for S&P 500 Futures and Treasury Futures.
- **Cumulative Returns and Drawdowns**: Plots cumulative returns and ongoing drawdowns for individual assets and the portfolio.
- **Rolling Sharpe Ratio**: Visualizes the rolling Sharpe Ratio for different time windows.

### 3. Statistical Analysis
- **Sharpe Ratio**: Calculates and prints the Sharpe Ratio for both individual assets and the portfolio.
- **Skewness and Kurtosis**: Computes and prints skewness and kurtosis for portfolio returns.
- **Drawdown**: Measures and visualizes maximum drawdown for the portfolio.

### 4. Inflation Adjustment
- **Inflation Data**: Fetches CPI data from FRED, calculates annualized inflation, and adjusts the Sharpe Ratio for inflation.

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
- Project Link: https://github.com/giovannamelob/Python-Projects/tree/main/AdvancedPortfolioAnalysis
