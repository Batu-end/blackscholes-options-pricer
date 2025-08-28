# Black-Scholes Option Pricer

## Overview
This app allows users to explore the ***Black-Scholes model*** for pricing options. It provides interactive widgets for input variables and visualizes the resulting option prices using a heatmap.

The app is designed to help users understand how key parameters—such as stock price, strike price, volatility, and risk-free rate—impact option pricing.

---

## Features
- **Interactive widgets**: Adjust parameters like stock price, volatility, and risk-free rate using intuitive sliders.
- **Dynamic Heatmaps**: Visualize option prices with real-time Seaborn heatmaps.
- **Real-Time Call/Put Pricing**: Instantly compute and compare option prices using the Black-Scholes model.

---

## The Black-Scholes Formula

> The Black-Scholes model, developed by Fischer Black and Myron Scholes, revolutionized options pricing in finance. Later, Robert Merton expanded upon their work by introducing mathematical refinements and applying the model more broadly. Together, the Black-Scholes-Merton framework became the cornerstone of modern financial theory...

### Mathematical Formula
<p align="center">
  <img src="./images/Black-Scholes-Formula.png" alt="Black-Scholes Formula" width="600">
</p>

To learn more about the math behind the model, see [**Wikipedia**](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) or [**Investopedia**](https://www.investopedia.com/terms/b/blackscholes.asp).

---

## Tech Stack
* **Framework:** [Streamlit](https://streamlit.io/)
* **Data Manipulation:** [NumPy](https://numpy.org/) & [Pandas](https://pandas.pydata.org/)
* **Visualization:** [Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/)
* **Financial Computation:** [SciPy](https://scipy.org/)

---

If you want to learn more about the formula, or are curious of the deeper math behind it, I strongly advise outside sources such as [***Wikipedia***](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) or [**_Investopedia_**](https://www.investopedia.com/terms/b/blackscholes.asp).

---

## 🚀 [Click Here for the Live Application](https://blackscholesoptionpricer.streamlit.app/)
