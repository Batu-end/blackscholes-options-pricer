import streamlit as st
from blackscholes import BS_CALL, BS_PUT
import data
from heatmap import heatmap_plot_call, heatmap_plot_put

# Titles, descriptions, and links
st.image("./images/linkedin_logo.png", width=50)
st.write("[Batu Demirtas](https://www.linkedin.com/in/batu-demirtas-ba83812ba/)")
st.title("Black-Scholes Option Pricing Model")
st.write("This is a simple ***Black-Scholes*** option pricing model calculator.")
st.write("You can use this app to calculate the price of a **European** call or put option based on the ***Black-Scholes*** formula.")
st.write("For more information about the ***Black-Scholes model***, please refer to the [***Investopedia article***](https://www.investopedia.com/terms/b/blackscholes.asp).")

# Input parameters for the user
S = st.slider("Current Asset Price (S)", min_value=50, max_value=200, value=100)
K = st.slider("Strike Price (K)", min_value=50, max_value=200, value=100)
T = st.slider("Time to Maturity (Years)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
sigma = st.slider("Volatility (σ)", min_value=0.1, max_value=1.0, value=0.25, step=0.01)
r = st.slider("Risk-Free Interest Rate (r)", min_value=0.0, max_value=0.1, value=0.05, step=0.01)


st.subheader("Heatmap Ranges")
min_spot_price = st.slider("Min Spot Price", min_value=50, max_value=200, value=80)
max_spot_price = st.slider("Max Spot Price", min_value=50, max_value=200, value=120)
min_volatility = st.slider("Min Volatility for Heatmap", min_value=0.1, max_value=1.0, value=0.1, step=0.01)
max_volatility = st.slider("Max Volatility for Heatmap", min_value=0.1, max_value=1.0, value=0.5, step=0.01)

option_type = st.selectbox("Option Type", ["Call", "Put"])

# data generation and heatmap deployment
if st.button("Plot Heatmap"):
    try:
        st.write("Generating heatmap...")
        if option_type == "Call":
            call_data = data.prepare_call_data(min_spot_price, max_spot_price, min_volatility, max_volatility, K, T, r)
            fig=heatmap_plot_call(call_data)
            st.pyplot(fig)
        elif option_type == "Put":
            put_data = data.prepare_put_data(min_spot_price, max_spot_price, min_volatility, max_volatility, K, T, r)
            fig=heatmap_plot_put(put_data)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred while generating the heatmap: {e}")