# Optimized Portfolio Value at Risk (VaR)

## Project Overview
This project focuses on optimizing a portfolio by minimizing the Value at Risk (VaR) using historical stock data. The analysis involves downloading historical data for a list of stocks, calculating daily log returns, and applying optimization techniques to minimize VaR. Additionally, the project calculates the expected return of the optimized portfolio.

## Tools and Libraries Used
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations and calculations.
- **yfinance**: For downloading historical stock data.
- **scipy**: For optimization techniques.

## Project Details

### 1. Data Retrieval and Preparation
- **Data Download**: Fetches historical data for a selection of stocks.
- **Return Calculation**: Computes daily logarithmic returns and handles missing values by forward filling and dropping.

### 2. Portfolio Optimization
- **VaR Calculation**: Calculates the Value at Risk for the portfolio based on given weights.
- **Optimization**: Uses the `minimize` function from `scipy.optimize` to find the weights that minimize the VaR of the portfolio.

### 3. Bonus Steps
- **Minimized VaR**: Outputs the minimized VaR of the portfolio with optimized weights.
- **Expected Return**: Calculates and prints the expected return of the optimized portfolio.

## Setup and Installation

Ensure you have Python installed and then install the necessary Python packages:

```bash
pip install -r requirements.txt
