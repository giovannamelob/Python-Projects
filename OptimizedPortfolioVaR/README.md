# Optimized Portfolio Value at Risk (VaR)

## Project Overview
This project implements a portfolio optimization technique using Value at Risk (VaR) minimization. It retrieves historical stock data for a set of tickers, calculates log returns, and optimizes the portfolio's weights to minimize its VaR using the Sequential Least Squares Programming (SLSQP) method from the `scipy.optimize` package.

## Getting Started

### Prerequisites
- Python 3.6+
- An active internet connection to fetch financial data.

### Installation
To run these scripts, you will need to install several Python libraries. The easiest way to install these is by using pip and the requirements file included in this repository:
pip install -r requirements.txt

## Project Details

### 1. Data Retrieval and Analysis
- **Historical Data**: Downloads adjusted closing prices for a list of 30 stock tickers from Yahoo Finance between the specified start and end dates.
- **Log Returns**: Computes daily logarithmic returns for the stocks, forward-fills any missing values, and drops rows with NA values to ensure clean data.

### 2. Portfolio VaR Minimization
- **VaR Calculation**: The project defines a function to calculate the portfolio's Value at Risk (VaR) based on the given confidence level (95% by default).
- **Optimization**: Uses the `scipy.optimize.minimize` function to minimize the portfolio's VaR by adjusting the portfolio's weights, with constraints on the sum of weights and bounds for each weight (optional).

### 3. Bonus Calculations
- **Minimized VaR**: After optimization, the project calculates and prints the minimized portfolio VaR.
- **Expected Return**: Optionally calculates the expected return for the optimized portfolio based on the optimized weights.

## Contributing
We welcome contributions from the community. Here are some guidelines you should follow:

1. **Fork the Repository**: Create a fork of our repository on your own GitHub account. This allows you to experiment with changes without affecting the original project.
2. **Make Changes**: Make your modifications in your forked repository. Please keep your changes concise and make sure they follow the existing project structure.
3. **Submit a Pull Request**: Once you are ready, submit a pull request to our repository. Include a clear description of the changes and the benefits they provide.

### Pull Request Guidelines
- Ensure that your code is well-documented and adheres to the existing style.
- Update the README.md if necessary.
- Add comments to your code where necessary to explain complex logic.

## License
This project is released under the MIT License. This allows you to use and modify the software freely for personal and commercial purposes under the conditions listed in the LICENSE file in this repository.

## Contact
- Giovanna  - melobenitesgiovanna@gmail.com
- Project Link: https://github.com/giovannamelob/Python-Projects/tree/main/OptimizedPortfolioVaR
