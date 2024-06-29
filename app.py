import streamlit as st 

import pandas as pd

dataset = pd.read_csv("apple_products.csv")

st.dataframe(dataset)