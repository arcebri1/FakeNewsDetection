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

# dic = {'Fakes News':10044, 'Real News':12229}
# keys = dic.keys()
# values = dic.values()

# plt.bar(keys, values)

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

# alt.Chart(source).mark_bar().encode(
#     x = 'x',
#     y = 'y'
# )

# plt.bar(x_axis, fake_real)

# amount = [5000, 10000, 15000]
# ypos = np.arange(len(label))
# plt.bar(ypos, amount)

# st.bar_chart(fake_news['Headline'])

# load_data.value_counts()

# data

# st.write(data)