import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# handles visualiation of the data through a seaborn heatmap
def heatmap_plot_call(data):

    plt.figure(figsize=(10, 8))
    sb.heatmap(data, cmap="coolwarm", annot=True, fmt=".1f", cbar=True,)
    plt.xlabel("Volatility (σ)", fontsize=12)
    plt.ylabel("Spot Price", fontsize=12)
    plt.title("Call Pricing", fontsize=16)

    return plt

def heatmap_plot_put(data):
    
    plt.figure(figsize=(10, 8))
    sb.heatmap(data, cmap="coolwarm", annot=True, fmt=".1f", cbar=True,)
    plt.xlabel("Volatility (σ)", fontsize=12)
    plt.ylabel("Spot Price", fontsize=12)
    plt.title("Put Pricing", fontsize=16)

    return plt