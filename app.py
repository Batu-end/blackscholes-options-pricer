import streamlit as st
from blackscholes import BS_CALL, BS_PUT
# from data import create_data_heatmap
# from heatmap import heatmap_plot

st.image("./images/linkedin_logo.png", width=50)
st.write("[Batu Demirtas](https://www.linkedin.com/in/batu-demirtas-ba83812ba/)")
st.title("Black-Scholes Option Pricing Model")
st.write("This is a simple ***Black-Scholes*** option pricing model calculator.")
st.write("You can use this app to calculate the price of a **European** call or put option based on the ***Black-Scholes*** formula.")
st.write("For more information about the ***Black-Scholes model***, please refer to the [***Investopedia article***](https://www.investopedia.com/terms/b/blackscholes.asp).")

# Input parameters for the user
S = st.slider("Stock Price (S)", min_value=50, max_value=200, value=100)
r = st.slider("Risk-Free Interest Rate in % (r)", min_value=0.0, max_value=0.1, value=0.05)
sigma = st.slider("Volatility in % (σ)", min_value=0.05, max_value=0.5, value=0.25)
option_type = st.selectbox("Option Type", ["Call", "Put"])

# data generation and heatmap deployment
# data = create_data_heatmap(S, r, sigma, option_type)