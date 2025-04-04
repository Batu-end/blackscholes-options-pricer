import numpy as np
import pandas as pd
from blackscholes import BS_CALL, BS_PUT

# Prepare data for call and put options
def prepare_call_data(min_spot_price, max_spot_price, min_volatility, max_volatility, K, T, r):

    spot_prices = np.linspace(min_spot_price, max_spot_price, 15)
    volatilities = np.linspace(min_volatility, max_volatility, 15)

    call_data_prepared = pd.DataFrame(
        [(spot, vol, BS_CALL(spot, K, T, r, vol)) 
         for spot in spot_prices for vol in volatilities],
        columns=["Spot Price", "Volatility", "Call Price"]
    ).pivot(index="Spot Price", columns="Volatility", values="Call Price")

    call_data_prepared.index = call_data_prepared.index.round(2)
    call_data_prepared.columns = call_data_prepared.columns.round(2)

    return call_data_prepared

def prepare_put_data(min_spot_price, max_spot_price, min_volatility, max_volatility, K, T, r):

    spot_prices = np.linspace(min_spot_price, max_spot_price, 15)
    volatilities = np.linspace(min_volatility, max_volatility, 15)

    put_data_prepared = pd.DataFrame(
        [(spot, vol, BS_PUT(spot, K, T, r, vol)) 
         for spot in spot_prices for vol in volatilities],
        columns=["Spot Price", "Volatility", "Put Price"]
    ).pivot(index="Spot Price", columns="Volatility", values="Put Price")

    put_data_prepared.index = put_data_prepared.index.round(2)
    put_data_prepared.columns = put_data_prepared.columns.round(2)

    return put_data_prepared