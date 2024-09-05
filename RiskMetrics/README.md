# Financial Risk Metrics

## Project Overview
This project focuses on calculating and analyzing various financial risk metrics using Python. The key metrics include Value at Risk (VaR), Expected Shortfall (ES), Delta VaR, Delta Stress ES, and Sharpe Ratios for different assets and portfolios. The project also includes visualization of cumulative returns, drawdowns, and rolling Sharpe Ratios, as well as inflation adjustment for the Sharpe Ratio.

## Tools and Libraries Used
- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical operations.
- **matplotlib**: Plotting and visualization.
- **yfinance**: Downloading historical financial data.
- **scipy**: Statistical calculations, including skewness and kurtosis.
- **pandas_datareader**: Fetching economic data (e.g., inflation rates).

## Project Details

### 1. Risk Metrics Calculation
- **VaR (Value at Risk)**: Measures potential loss at a specified confidence level.
- **ES (Expected Shortfall)**: Average loss beyond the VaR.
- **Delta VaR**: Change in VaR with a shift in returns.
- **Delta Stress ES**: Change in ES with a shift in returns.

### 2. Visualization
- **Return Distributions**: Histograms and KDE plots of returns.
- **Cumulative Returns and Drawdowns**: Plots for individual assets and portfolios.
- **Rolling Sharpe Ratio**: Rolling Sharpe Ratios over different time windows.

### 3. Statistical Analysis
- **Sharpe Ratio**: Calculates the Sharpe Ratio for assets and portfolios.
- **Skewness and Kurtosis**: Measures of the return distribution's shape.
- **Drawdown Analysis**: Calculates and plots maximum drawdown.

### 4. Inflation Adjustment
- **Inflation Data**: Fetches CPI data and adjusts the Sharpe Ratio for inflation.

## Setup and Installation

Ensure you have Python installed and then install the necessary Python packages:

```bash
pip install -r requirements.txt
