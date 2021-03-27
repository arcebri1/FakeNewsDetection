import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt


st.title('Fake News Detection')

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv('merged_data.csv', nrows=nrows)
    return data

fake_news = load_data(1000)

st.subheader('Fake News Article Data')
st.write(fake_news)


# fake = load_data['label'] == 0

# label = ['Fake News', 'Real News']
# fake_real = [10044, 12229]
# x_axis = np.arange(len(label)) 
# st.write(x_axis)
# st.bar_chart(x_axis,fake_real)

st.subheader('Total Amount of Type of Articles')
source = pd.DataFrame({
    'x': ['Fake News', 'Real News'],
    'y': [10044, 12229]
})

source 

st.bar_chart(source)



news = ['Fake', 'Real']
amount = [10044, 12229]

# st.write(news)
