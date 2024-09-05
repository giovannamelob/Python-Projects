# Ethereum Time Series Analysis and Forecasting

## Project Overview
This project analyzes Ethereum's historical price data using various time series analysis techniques. The analysis includes handling missing data, plotting trends, applying rolling statistics, decomposing the time series into components, and building an ARIMA model to predict future prices. It utilizes data sourced from Yahoo Finance and performs a variety of statistical and graphical analyses to understand Ethereum's price movement.

## Getting Started

### Installation
To run these scripts, you will need to install several Python libraries. The easiest way to install these is by using pip and the requirements file included in this repository:
pip install -r requirements.txt

## Project Details

### 1. Data Retrieval and Handling
- **Ethereum Data**: The project imports Ethereum price data from a CSV file and ensures that the index is unique and monotonic.
- **Handling Duplicates**: Removes duplicate rows and non-monotonic indexes, reindexing and filling gaps in the data using forward fill.
- **Dynamic Time Slicing**: Allows users to dynamically slice the dataset and visualize Ethereum's price over different time ranges.

### 2. Visualization
- **Plotting Close Prices**: Plots the closing price of Ethereum over time with various overlays such as 50-day and 200-day moving averages.
- **Resampling and Aggregation**: Resamples the data at hourly and daily frequencies, calculating metrics such as mean, standard deviation, and OHLC (Open, High, Low, Close) values.

### 3. Time Series Analysis
- **Rolling Statistics**: Calculates and plots the rolling mean and standard deviation to observe trends and volatility over time.
- **Seasonal Decomposition**: Decomposes the time series into trend, seasonal, and residual components using additive modeling.
- **Autocorrelation and Partial Autocorrelation**: Plots autocorrelation and partial autocorrelation to identify patterns and dependencies in the data.

### 4. Forecasting with ARIMA Model
- **ARIMA Model**: Fits an ARIMA(5,1,0) model to the data for future price predictions. The ARIMA model helps in forecasting future values based on historical data trends.
- **Prediction**: Plots the original closing prices along with predicted future values for a 30-day forecast using the ARIMA model.

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
- Project Link: https://github.com/giovannamelob/Python-Projects/tree/main/Project1-Data-Wrangling
