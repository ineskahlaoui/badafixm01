

from urllib.error import URLError

import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import exploration_plots as exp

import streamlit as st

from streamlit.hello.utils import show_code

st.set_page_config(page_title="Data Exploration", page_icon="📊")
st.markdown("# Data Exploration")
st.sidebar.header("Data Exploration")

@st.cache_data
def get_data():
    df = pd.read_csv('data/MS_prep.csv')
    return df

movies_summary = get_data()


st.title("Movie Trends Analysis")
exp.plot_generations_movie_releases(movies_summary)

st.title("Sentiment score")
exp.sentiment_score_distribution(movies_summary)

