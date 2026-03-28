# YouTube Trending Videos Analytics Dashboard

This Streamlit dashboard visualizes insights from a YouTube Trending Videos dataset. It allows users to explore trends in likes over time, view top-performing videos, and analyze yearly and monthly engagement.

---

## Features

- **Monthly Likes Trend:** Line chart showing the total likes per month.  
- **Yearly Likes Overview:** Bar chart with a logarithmic Y-axis to handle large differences in yearly likes.  
- **Top 5 Videos by Likes:** Bar chart displaying the five videos with the highest likes.  
- **Interactive & Responsive:** Built using Plotly and Streamlit for an interactive experience.  

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```
## Dataset

The dataset used in this dashboard is sourced from [Kaggle's YouTube Trending Videos](https://www.kaggle.com/datasets/thedevastator/youtube-trending-videos-dataset). It contains information about trending videos, including their titles, publish times, views, likes, and more.