# Black-Scholes Option Pricing Streamlit App

## Overview
This Streamlit app allows users to explore the **Black-Scholes model** for option pricing. It provides interactive widgets for input variables and visualizes the resulting option prices using a **Seaborn heatmap**.

The app is designed to help users understand how key parameters—such as stock price, strike price, volatility, and risk-free rate—impact option pricing.

---

## Features
- ** **: 
- ** **:
- ****:

---

# Black-Scholes Option Pricing Formula

The Black-Scholes formula calculates the theoretical price of European call and put options.

### Call Option Formula:


\[ C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2) \]



### Put Option Formula:


\[ P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1) \]



### Where:
- \( d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \)
- \( d_2 = d_1 - \sigma\sqrt{T} \)

### Variables:
- \( S \): Current stock price
- \( K \): Strike price
- \( T \): Time to expiration (in years)
- \( r \): Risk-free interest rate
- \( \sigma \): Volatility of the stock price
- \( N(x) \): Cumulative standard normal distribution

---

## Getting Started
Follow the steps below to run the app locally:

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Pip package manager

Install the required libraries:
```bash
pip install streamlit numpy pandas seaborn matplotlib scipy
