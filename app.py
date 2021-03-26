import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

st.title('Fake News Detection')

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv('merged_data.csv', nrows=nrows)
    return data

fake_news = load_data(1000)

st.subheader('Fake News Article Data')
st.write(fake_news)

# data

# st.write(data)