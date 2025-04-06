# Black-Scholes Option Pricing Streamlit App

## Overview
This Streamlit app allows users to explore the **Black-Scholes model** for option pricing. It provides interactive widgets for input variables and visualizes the resulting option prices using a **Seaborn heatmap**.

The app is designed to help users understand how key parameters—such as stock price, strike price, volatility, and risk-free rate—impact option pricing.

---

## Features
- **Interactive widgets**: Adjust parameters like stock price, volatility, and risk-free rate using intuitive sliders.
- **Dynamic Heatmaps**: Visualize option prices with real-time Seaborn heatmaps.
- **Real-Time Call/Put Pricing**: Instantly compute and compare option prices using the Black-Scholes model.

---

# Black-Scholes Option Pricing Formula

The *Black-Scholes model*, developed by Fischer Black and Myron Scholes, revolutionized options pricing in finance. Later, _Robert Merton_ expanded upon their work by introducing mathematical refinements and applying the model more broadly. Together, the _Black-Scholes-Merton_ framework became the cornerstone of modern financial theory and remains widely used for pricing _European-style_ options and managing financial risk.

If you want to learn more about it, you I strongly advise outside sources such as [***Wikipedia***](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) or [**_Investopedia Article_**](https://www.investopedia.com/terms/b/blackscholes.asp).

Below is the mathematical representation of the option pricing model.

![Black-Scholes Formula](./images/Black-Scholes-Formula.png)

## Getting Started
1. Move into a directory and clone the repository:
   ```bash
   git clone https://github.com/Batu-end/blackscholes-options-pricer.git
