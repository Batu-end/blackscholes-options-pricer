import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

def heatmap_plot(data):
    plt.figure(fihgsize=(10, 8))
    sb.heatmap(data, cmap="coolwarm", annot=True)
    st.pyplot(plt)