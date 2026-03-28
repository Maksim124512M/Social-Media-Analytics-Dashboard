import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache_data
def load_dataframe():
    df = pd.read_csv('data/youtube.csv')
    df = df.drop_duplicates(['title'])

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

df['publish_date'] = pd.to_datetime(df['publish_date'], dayfirst=True)
df['publish_month'] = df['publish_date'].dt.month
df['publish_year'] = df['publish_date'].dt.year

monthly_likes = df.groupby('publish_month')['likes'].sum()
yearly_likes = df.groupby('publish_year')['likes'].sum()

top_five_videos_by_likes = df.sort_values(by='likes', ascending=False)[:5]

figure = make_subplots(
    rows=3, cols=1,
    subplot_titles=('Likes by month', 'Likes by year', 'TOP-5 videos by likes'),
    row_heights=[0.5, 0.25, 0.25]
)

figure.add_trace(go.Scatter(
    x=monthly_likes.index,
    y=monthly_likes.values,
    mode='lines+markers',
    name='Likes by month',
), row=1, col=1)

figure.add_trace(go.Bar(
    x=yearly_likes.index,
    y=yearly_likes.values,
    name='Likes by year',
), row=2, col=1)
figure.update_yaxes(type='log')

figure.add_trace(go.Bar(
    x=top_five_videos_by_likes['video_id'],
    y=top_five_videos_by_likes['likes'],
    name='Likes',
), row=3, col=1)

figure.update_layout(
    title='YouTube Trending Videos Dataset Analytics',
    template='plotly_dark',
    height=900,
)

st.plotly_chart(figure)