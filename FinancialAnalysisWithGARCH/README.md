# Financial Analysis with GARCH

## Project Overview
This project implements various financial analysis techniques including Walk-Forward Validation, Risk-Parity Portfolio construction, and the application of the GARCH (Generalized Autoregressive Conditional Heteroskedasticity) model. The focus is on analyzing historical stock and futures data, calculating excess returns, and evaluating risk-adjusted performance metrics.

## Tools and Libraries Used
- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical operations.
- **yfinance**: Downloading financial data.
- **matplotlib**: Plotting and visualization.
- **seaborn**: Advanced data visualization.
- **scipy**: Statistical tests.
- **arch**: GARCH model for volatility clustering.

## Project Details

### Data Analysis
- **Download Data**: Fetches historical data for Berkshire Hathaway stock and S&P 500 front month futures.
- **Log Returns**: Computes daily logarithmic returns for the stocks and futures.
- **Excess Returns**: Calculates excess returns over the risk-free rate.
- **Information Ratio**: Evaluates performance with the Information Ratio.

### Visualizations
- **Return Distributions**: Histograms and KDE plots of returns for Berkshire Hathaway and S&P 500 futures.
- **Cumulative Returns**: Plots cumulative returns for Berkshire Hathaway, S&P 500 futures, and other portfolios.
- **Correlation Matrix**: Heatmap of correlation between FAANG stocks.

### Statistical Analysis
- **t-Test**: Performs a t-test on portfolio returns to check if the mean return is significantly different from zero.

### Volatility Clustering
- **GARCH Model**: Fits a GARCH model to portfolio returns to analyze volatility clustering and plots the conditional volatility.

## Setup and Installation

Ensure you have Python installed and then install the necessary Python packages:

```bash
pip install -r requirements.txt
