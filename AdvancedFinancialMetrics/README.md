# Advanced Financial Metrics

## Project Overview
This project encompasses a series of Python scripts designed to analyze financial data for different investment instruments, including S&P 500 Futures, 10-Year Treasury Futures, and a diversified investment portfolio. The analysis includes calculating Sharpe Ratios, annualized returns, and portfolio risk metrics, adjusted for inflation and risk-free rates.

## Tools and Libraries Used
Ensure you have Python 3.6+ installed on your system. The following Python libraries are required:
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib**: For plotting and visualization.
- **yfinance**: For downloading financial data.
- **scipy**: For statistical calculations, including skewness and kurtosis.
- **pandas_datareader**: For fetching inflation data from FRED.

### Installation
Clone this repository and install the required Python packages:

```bash
git clone https://github.com/yourusername/financial-data-analysis.git
cd financial-data-analysis
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
