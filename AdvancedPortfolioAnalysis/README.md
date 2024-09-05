# Advanced Portfolio Analysis

## Project Overview
This project focuses on advanced portfolio analysis and optimization using Python. It includes the calculation of various financial metrics such as Value at Risk (VaR), Expected Shortfall (ES), and Sharpe Ratios. Additionally, it performs Monte Carlo simulations to visualize the Efficient Frontier and applies advanced techniques for portfolio optimization, risk contribution analysis, and stress testing.

## Tools and Libraries Used
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib**: For plotting and visualization.
- **seaborn**: For advanced visualizations.
- **yfinance**: For downloading historical financial data.
- **scipy**: For statistical calculations, including skewness and kurtosis.
- **pandas_datareader**: For fetching economic data (e.g., inflation rates).

## Project Details

### 1. Data Retrieval and Processing
- **Data Download**: Fetches historical data for selected stocks and futures.
- **Return Calculation**: Computes daily logarithmic returns.
- **Risk Metrics**: Calculates VaR, ES, Delta VaR, and Delta Stress ES.

### 2. Portfolio Optimization
- **Random Portfolios**: Generates and evaluates 10,000 portfolios to identify optimal portfolios based on Sharpe Ratio and Minimum Variance.
- **Optimization with Constraints**: Uses optimization techniques to find the optimal portfolio weights with constraints.

### 3. Visualization
- **Markowitz Efficient Frontier**: Plots the Efficient Frontier with portfolio return and volatility.
- **Portfolio Drawdowns**: Visualizes cumulative returns and drawdowns for portfolios.
- **Monte Carlo Simulation**: Simulates and visualizes a range of portfolios and their performance on the Efficient Frontier.

### 4. Statistical Analysis
- **Sharpe Ratio**: Calculates the Sharpe Ratio for individual assets and portfolios.
- **Skewness and Kurtosis**: Measures the skewness and kurtosis of return distributions.
- **Inflation Adjustment**: Adjusts Sharpe Ratio for inflation.

## Setup and Installation

Ensure you have Python installed and then install the necessary Python packages:

```bash
pip install -r requirements.txt
