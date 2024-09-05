# Financial Analysis with GARCH

## Project Overview
This project analyzes Berkshire Hathaway's stock performance relative to S&P 500 futures using advanced financial metrics, including the Information Ratio and volatility clustering via GARCH modeling. It includes return distributions, cumulative return plots, correlation analysis, statistical tests, and volatility clustering for FAANG portfolios.

## Getting Started

### Prerequisites
- Python 3.6+
- An active internet connection to fetch financial data.

### Installation
To run these scripts, you will need to install several Python libraries. The easiest way to install these is by using pip and the requirements file included in this repository:
pip install -r requirements.txt


## Project Details

### 1. Data Retrieval and Analysis
- **Berkshire Hathaway vs. S&P 500 Futures**: The project downloads stock data for Berkshire Hathaway and S&P 500 futures, computes the daily logarithmic returns, excess returns, and annualized excess returns.
- **Information Ratio**: Calculates the Information Ratio, which compares the performance of Berkshire Hathaway relative to the S&P 500 futures based on annualized excess returns and tracking error.

### 2. Visualization
- **Return Distributions**: Plots histograms with KDE (Kernel Density Estimation) for both Berkshire Hathaway and S&P 500 futures' returns.
- **Cumulative Returns**: Visualizes the cumulative returns for Berkshire Hathaway, S&P 500 futures, FAANG portfolios, and the NASDAQ.
- **Correlation Matrix**: Computes and visualizes the correlation matrix for FAANG stocks using a heatmap.

### 3. Statistical Analysis
- **t-test**: Performs a one-sample t-test to determine whether the FAANG portfolio returns are significantly different from zero.
  
### 4. Volatility Clustering (GARCH Model)
- **GARCH Model**: Fits a GARCH(1,1) model to the FAANG portfolio returns to analyze volatility clustering. Conditional volatility is plotted over time to capture fluctuations in portfolio risk.

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
- Giovanna Melo Benites - melobenitesgiovanna@gmail.com
- Project Link: https://github.com/giovannamelob/Python-Projects/tree/main/FinancialAnalysisWithGARCH
