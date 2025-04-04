import streamlit as st
import data
from heatmap import heatmap_plot_call, heatmap_plot_put
import base64

# Titles, descriptions, and links
st.title(":green[*Black-Scholes Option Pricing Model*]")
st.markdown("---")
st.subheader("This is a :grey[***Black-Scholes***] option pricing model calculator.")
st.subheader("You can use this web app to calculate the price of a :blue[**European**] call or put option based on the ***Black-Scholes*** formula.")
st.subheader("For more information about the ***Black-Scholes model***, please refer to the [***Investopedia article***](https://www.investopedia.com/terms/b/blackscholes.asp) about it.")

st.markdown("---")

# Input parameters for the user
S = st.slider("Current Asset Price (S)", min_value=50, max_value=200, value=100, key="slider_S")
K = st.slider("Strike Price (K)", min_value=50, max_value=200, value=100, key="slider_K")
T = st.slider("Time to Maturity (Years)", min_value=0.1, max_value=5.0, value=1.0, step=0.1, key="slider_T")
r = st.slider("Risk-Free Interest Rate (r)", min_value=0.0, max_value=0.1, value=0.05, step=0.01, key="slider_r")
sigma = st.slider("Volatility (σ)", min_value=0.1, max_value=1.0, value=0.25, step=0.01, key="slider_sigma")

# Calculate call and put prices dynamically
call_price = data.BS_CALL(S, K, T, r, sigma)
put_price = data.BS_PUT(S, K, T, r, sigma)

# Initialize session state for previous call and put prices
if "prev_call_price" not in st.session_state:
    st.session_state["prev_call_price"] = call_price
if "prev_put_price" not in st.session_state:
    st.session_state["prev_put_price"] = put_price

# Personal links and dynamic calculation of call and put prices
with st.sidebar:
        
        st.subheader("*Batu Demirtas*")

        # LinkedIn hyperlink logo
        linkedin_html = """
            <a href="https://www.linkedin.com/in/batu-demirtas-ba83812ba/">
                <img src="data:image/png;base64,{}" width="50">
            </a>
        """

        with open("./images/linkedin_logo.png", "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        st.sidebar.markdown(linkedin_html.format(encoded_image), unsafe_allow_html=True)

        st.write(" ")

        # GitHub hyperlink logo
        github_html = """
            <a href="https://github.com/Batu-end/blackscholes-options-pricer">
                <img src="data:image/png;base64,{}" width="50">
            </a>
        """

        with open("./images/github_logo.png", "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        st.sidebar.markdown(github_html.format(encoded_image), unsafe_allow_html=True)

        st.write(" ")

        # X hyperlink logo
        x_html = """
            <a href="https://twitter.com/finansender">
                <img src="data:image/png;base64,{}" width="50">
            </a>
        """

        with open("./images/x_logo.png", "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        st.sidebar.markdown(x_html.format(encoded_image), unsafe_allow_html=True)

        st.markdown("---")

        # Prepare delta values to show the change in prices
        call_delta = call_price - st.session_state["prev_call_price"]
        put_delta = put_price - st.session_state["prev_put_price"]

        # Display prices dynamically in the sidebar
        st.metric(label="Call Price", value=f"${call_price:.2f}", delta=f"+${call_delta:.2f}", delta_color="normal")
        st.metric(label="Put Price", value=f"${put_price:.2f}", delta=f"-${put_delta:.2f}", delta_color="normal") # not inverse since we already multiplied by -1

st.subheader("Heatmap Ranges")
min_spot_price = st.slider("Min Spot Price", min_value=50, max_value=200, value=80, key="slider_min_spot_price")
max_spot_price = st.slider("Max Spot Price", min_value=50, max_value=200, value=120, key="slider_max_spot_price")
min_volatility = st.slider("Min Volatility for Heatmap", min_value=0.1, max_value=1.0, value=0.1, step=0.01, key="slider_min_volatility")
max_volatility = st.slider("Max Volatility for Heatmap", min_value=0.1, max_value=1.0, value=0.5, step=0.01, key="slider_max_volatility")

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