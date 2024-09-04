# Time Series Data Analysis on Ethereum Prices

## Project Overview
This project focuses on performing time series analysis on Ethereum (ETH) price data using Python. The dataset consists of historical ETH prices, and the analysis involves data cleaning, resampling, visualization, and more advanced statistical methods like autocorrelation analysis. The goal is to demonstrate key techniques used in time series analysis for financial data, including handling missing data, resampling, moving averages, and checking for autocorrelation.

## Tools and Libraries Used
- **Pandas**: For data manipulation and wrangling.
- **Numpy**: For numerical operations.
- **Matplotlib**: For visualizations and plotting.
- **Statsmodels**: For autocorrelation and partial autocorrelation analysis.

## Setup Instructions

To run this project, you will need to install the required Python libraries. Please ensure you have Python installed on your system, and then run the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt

## Sections of the Project
### 1. Data Loading and Initial Exploration
- The data is loaded from a CSV file using pandas. The `open_time` column is parsed as a date and used as the index.
- Initial checks are performed to ensure the index is unique and sorted, and the overall shape of the dataset is explored.

### 2. Data Visualization
- A basic line plot of Ethereum's close prices over time is generated using matplotlib. This provides a visual understanding of how the prices evolve over time.

### 3. Resampling and Moving Averages
- The close prices are resampled by different frequencies (daily, hourly, monthly) to analyze the average price trends over time.
- A 7-day moving average is calculated and plotted alongside the daily close price to observe price smoothing and trends over time.

### 4. Handling Missing Data
- Various methods are employed to handle missing data (or discontinuities):
  - **Interpolation**: Using linear interpolation to fill gaps.
  - **Forward Fill**: Filling missing values with the last observed non-null value.
  - **Backward Fill**: Filling missing values with the next observed non-null value.

### 5. Aggregation and Grouping
- Prices are grouped and aggregated over fixed time intervals (e.g., daily, hourly) using methods like mean, standard deviation, and OHLC (Open, High, Low, Close) aggregation.
- These techniques help summarize the dataset and extract key features over different periods of time.

### 6. Autocorrelation and Partial Autocorrelation Analysis
- Autocorrelation and partial autocorrelation are calculated to determine whether the data shows significant correlation with its own past values, which is key for financial modeling and forecasting.
  - **Autocorrelation** checks the relationship between current and past values in the series.
  - **Partial Autocorrelation** helps in understanding the direct correlation between the current value and past values, after accounting for the influence of intermediate values.

## Conclusion
This project showcases fundamental techniques in financial time series analysis, focusing on resampling, missing data handling, and statistical analysis like autocorrelation. By exploring Ethereum price data, the project demonstrates how to clean and analyze financial data for potential insights, and how these techniques can be applied to other financial datasets.
