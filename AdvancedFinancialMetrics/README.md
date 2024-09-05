# Advanced Financial Metrics

## Project Overview
This project performs comprehensive financial analysis using Python, focusing on calculating the Sharpe Ratio for S&P 500 Futures and 10-Year Treasury Futures, constructing and analyzing a 60-40 portfolio, and adjusting for inflation. The analysis includes rolling Sharpe Ratios, risk metrics, and visualizations of cumulative returns and drawdowns.

## Tools and Libraries Used
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib**: For plotting and visualization.
- **yfinance**: For downloading financial data.
- **scipy**: For statistical calculations, including skewness and kurtosis.
- **arch**: For GARCH modeling (if used in your project).
- **pandas_datareader**: For fetching inflation data from FRED.

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

## Setup and Installation

Ensure you have Python installed and then install the necessary Python packages:

```bash
pip install -r requirements.txt
