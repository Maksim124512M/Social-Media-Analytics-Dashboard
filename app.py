import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache_data
def load_dataframe():
    df = pd.read_csv('data/youtube.csv')
    df = df.drop_duplicates()

    return df


df = load_dataframe()

total_likes, avg_likes, top_video_by_likes = st.columns(3)
top_video = df.sort_values(by='likes', ascending=False).iloc[0]

total_likes.metric('Total likes', df['likes'].sum())
avg_likes.metric('Average likes per vider', round(df['likes'].mean(), 2))
top_video_by_likes.metric('TOP Video by likes', top_video['likes'])
top_video_by_likes.caption(f'{top_video['title']}')

video = st.selectbox('Select video', options=df['title'])

filtered_data = df[df['title'] == video]

st.metric('Likes of video', int(filtered_data['likes'].iloc[0]))

df['publish_date'] = pd.to_datetime(df['publish_date'])

# df_grouped_by_publish_date = df.groupby(df['publish_date'].dt.date)['likes'].sum()

