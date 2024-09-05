# Black Scholes Option Calculator

## Project Overview
This project implements the Black-Scholes option pricing model to calculate the theoretical prices of European call and put options. The model uses factors such as the underlying asset's price, the strike price, time to maturity, risk-free interest rate, and volatility to compute the option prices. 

## Getting Started

### Prerequisites
- Python 3.6+

### Installation
To run these scripts, you will need to install several Python libraries. The easiest way to install these is by using pip and the requirements file included in this repository:
pip install -r requirements.txt

## Project Details

### 1. Option Pricing
- **Black-Scholes Model**: This project implements the Black-Scholes formula to calculate the prices of European call and put options.
- **Call Option**: The model computes the price of a call option using the formula.
- **Put Option**: The model also computes the price of a put option using the same formula with adjusted parameters.

### 2. Input Parameters
The Black-Scholes model uses the following parameters:
- **S**: Initial stock price (spot price)
- **K**: Strike price
- **T**: Time to maturity (in years)
- **r**: Risk-free interest rate
- **vol**: Volatility (standard deviation of stock returns)
- **type**: Option type ('c' for Call, 'p' for Put)

### 3. Outputs
The project prints the calculated option prices for both call and put options.

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
- Your Name - your.email@example.com
- Project Link: https://github.com/giovannamelob/Python-Projects/tree/main/BlackScholesOptionCalculator

## Acknowledgments
- This project uses the Black-Scholes formula for option pricing, which is widely used in financial markets for pricing European-style options.
