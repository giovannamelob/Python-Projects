# Advanced Financial Analysis

## Project Overview
This project encompasses various financial analysis techniques using Python, including calculating returns, volatility, and risk metrics for stock and futures data. It also covers portfolio construction, drawdowns, and statistical measures such as skewness and kurtosis. Key features include analyzing S&P 500 futures, building a risk-parity portfolio, and visualizing returns and drawdowns.

## Tools and Libraries Used
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations and calculations.
- **matplotlib**: For data visualization.
- **seaborn**: For advanced visualizations (if used in any part of the code).
- **yfinance**: For downloading financial data.
- **arch**: For GARCH modeling.

## Project Details

### 1. Data Retrieval and Analysis
- **S&P 500 Futures**: Downloads and analyzes S&P 500 futures data.
- **Berkshire Hathaway**: Downloads and analyzes Berkshire Hathaway stock data.
- **FAANG Stocks**: Constructs a portfolio with FAANG stocks and calculates returns.
- **Volatility and Risk Metrics**: Computes annualized returns, volatility, and other risk metrics.

### 2. Visualization
- **Return Distributions**: Plots histograms and KDE plots of returns for visual analysis.
- **Cumulative Returns**: Visualizes cumulative returns and compares different portfolios.
- **Correlation Matrix**: Displays a heatmap of correlations between FAANG stocks.
- **Drawdowns**: Plots ongoing drawdowns for individual assets and portfolios.

### 3. Statistical Analysis
- **t-Test**: Performs a t-test on portfolio returns to determine statistical significance.
- **Skewness and Kurtosis**: Calculates and prints skewness and kurtosis of return distributions.

### 4. Volatility Clustering
- **GARCH Model**: Fits a GARCH model to portfolio returns and plots conditional volatility.

## Setup and Installation

Ensure you have Python installed and then install the necessary Python packages:

```bash
pip install -r requirements.txt
