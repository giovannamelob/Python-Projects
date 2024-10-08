# -*- coding: utf-8 -*-
"""Options Pricing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tp4R5oJJ0sdYGVjPbNKuErhsFNOo8ZTV

# Vanilla Option Pricing
"""

from datetime import datetime
import time
from scipy.stats import norm
import numpy as np

t = datetime(2022,3,1)
T2 = datetime(2022,12,31) #Maturity

# Initialise parameters
S0 = 130                # initial stock price
K0 = 130                # strike price
T0 = ((T2-t).days)/365     # time to maturity in years
r0 = 0.02                   # annual risk-free rate
vol = 0.08              # volatility (%)
q0=0.0

def blackScholes(r, S, K, T, sigma, type="c"):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
print("Black Scholes Option Price for CALL ATM: ", round(blackScholes(r0, S0, K0, T0, vol, "c"),2))

S0 = 131            # initial stock price
K = 130              # strike price
T = ((T2-t).days)/365     # time to maturity in years
r = 0.02                  # annual risk-free rate
vol = 0.08             # volatility (%)
q=0.0

def blackScholes(r, S, K, T, sigma, type="c"):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
print("Black Scholes Option Price for CALL ATM: ", round(blackScholes(r, S0, K, T, vol, "c"),2))

def blackScholes(r, S, K, T, sigma, type="p"):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
print("Black Scholes Option Price for PUT ATM: ", round(blackScholes(r, S0, K, T, vol, "p"),2))