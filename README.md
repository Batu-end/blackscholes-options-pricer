# Black-Scholes Option Pricer

## Overview
This app allows users to explore the ***Black-Scholes model*** for pricing European options. With a **beginner-friendly UI**, it provides interactive widgets for all input variables and visualizes the resulting option prices using dynamic heatmaps.

The app is designed to help users understand how key parameters—such as stock price, strike price, volatility, and risk-free rate—impact option pricing.

---

## 🚀 [Click Here for the Live Application](https://blackscholesoptionpricer.streamlit.app/)

---

## App Preview

The interface is designed to be intuitive. Simply choose an option type from the dropdown menu and adjust the sliders to see how the option's price changes in real-time.

<p align="center">
  <img src="./images/Dropdown.gif" alt="Dropdown Menu GIF" width="600">
  <br>
  <em>Select either a Call or Put option to begin.</em>
</p>

<p align="center">
  <img src="./images/Demo.gif" alt="Sliders GIF" width="600">
  <br>
  <em>Adjust financial parameters like volatility and interest rates with simple sliders.</em>
</p>

---

## The results are instantly visualized in a heatmap and compared directly in a summary table.
<p align="center">
  <img src="./images/PutMap.png" alt="Put Heatmap GIF" width="48%">
  <img src="./images/CallMap.png" alt="Call Heatmap" width="48%">
  <br>
  <em>Dynamic heatmaps for both Put (left) and Call (right) options.</em>
</p>

<p align="center">
  <img src="./images/Comparison.png" alt="Comparison of Results" width="30%">
  <br>
  <em>And topped off with an easy to follow comparison in USD$.</em>
</p>

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
