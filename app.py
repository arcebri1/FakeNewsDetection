import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
# import plotly.express as px


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

# source = pd.DataFrame({
#     'Fake News': [10044],
#     'Real News': [12229]
# })

source 

st.bar_chart(source)

st.line_chart(source)

st.area_chart(source)

##############

source1 = pd.DataFrame({
    'Type of Article': ['Fake News', 'Real News'],
    'Number of Articles': [10044, 12229]
})

bar = alt.Chart(source1).mark_bar(size=30).encode(
    x='Type of Article',
    y='Number of Articles',
    color=alt.Color('Number of Articles')
).properties(width=350)

st.write(bar)


# hist_data = [source[x],source[y]]
# group_labels = [‘Type of News’, ‘Number of News Articles’]
# fig = ff.create_distplot(hist_data, group_labels)
# st.plotly_chart(fig, use_container_width=True)


st.write("""
# Hello
Testing out
""")
##Cannot have the same key for selectboxes (Select Dataset)
#Drop-down box
data_set=st.selectbox("Select Dataset", ("Fake News", "Real News"))
# st.write(data_set)

#side bar drop-down
data_side=st.sidebar.selectbox("Select Data-set", ("Fake News", "Real News"))
# st.write(data_side)

classifier_name = st.sidebar.selectbox("Select Classifier", ('KNN','SVM','Random Forest'))



# def get_dataset(data_side):
#     if data_side == "Fake News":
#         data = datasets.load_fake_news()
#     elif data_side == "Real News":
#         data = datasets.load_real_news()
#     else:

news = ['Fake', 'Real']
amount = [10044, 12229]
# y_pos = np.arange(len)

# st.write(news)
