# Risk Parity Portfolio and Walk-Forward Validation

This project demonstrates advanced financial modeling techniques including Walk-Forward Validation and the construction of a Risk-Parity Portfolio using Python. The approach helps in ensuring robustness by mimicking real-world trading conditions and aims to evenly distribute risk across portfolio assets based on their volatilities.

## Project Overview

- **Walk-Forward Validation**: Segments historical data into training and testing phases to prevent lookahead bias and overfitting.
- **Risk Parity Portfolio**: Allocates weights inversely related to asset volatility, promoting an equal risk contribution from each asset.

## Tools and Libraries Used

- `pandas` for data manipulation.
- `numpy` for numerical calculations.
- `matplotlib` for visualizations.
- `yfinance` for downloading financial data.
- `scipy` for statistical calculations.

## Setup and Installation

Ensure you have Python installed and then install the necessary Python packages:

```bash
pip install -r requirements.txt
