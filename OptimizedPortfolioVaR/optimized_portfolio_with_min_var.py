# -*- coding: utf-8 -*-
"""Level 4 - Optimized portfolio with min VaR

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1igKnJmtqQqhcRPKx70zbPCWfK0EabmF5
"""

Final Project - Level 4 Assignment

Student: Giovanna Melo Benites

import yfinance as yf
import numpy as np
import pandas as pd
from scipy.optimize import minimize

tickers = ['NVDA','AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'ORCL', 'ABT', 'JNJ', 'WMT',
           'JPM', 'MMM', 'PG', 'UNH', 'DIS', 'AXP', 'PYPL', 'BAC', 'VZ',
           'ADBE', 'CMCSA', 'NFLX', 'KO', 'NKE', 'MRK', 'PEP', 'T', 'PFE', 'INTC', 'CSCO']

# Import historical data
data = yf.download(tickers, start="2021-04-29", end="2024-04-29")['Adj Close']

# Calculate daily log returns
returns = np.log(data/data.shift(1))

# Check for NA values, forward fill them if necessary and drop the others
# print(log_returns.isna().sum())
returns = returns.ffill()
returns = returns.dropna()

# Calculate portfolio_returns and VaR
def portfolio_var(weights, returns, confidence_level=0.95):
    portfolio_return = returns.dot(weights)   # matrix multiplication between the returns matrix and the weights vector

    var_level = 1 - confidence_level
    VaR = np.percentile(portfolio_return, var_level * 100)

    return VaR

# Minimize VaR -- This function works like Solver on Excel
result = minimize(fun=portfolio_var, x0=initial_weights, args=(returns, 0.95),
                  method='SLSQP', bounds=bounds, constraints=constraints)
  # minimize function portfolio_var by changing initial_weights
  # args = arguments to the portfolio_var function
  # 'SLSQP' stands for Sequential Least Squares Programming

# Check if the minimization was successful
# result.success == True

optimized_weights = result.x

print("Optimized Weights:", optimized_weights)
print("Minimized Portfolio VaR:", portfolio_var(optimized_weights, returns))

# Bonus Steps

# Calculate the minimized VaR with optimized weights
minimized_VaR = portfolio_var(result.x, returns, 0.95)
print("Minimized Portfolio VaR:", minimized_VaR)

# Calculate Expected Return for the optimized portfolio (optional)
expected_return = np.mean(returns.dot(result.x))
print("Expected Return of the Optimized Portfolio:", expected_return)