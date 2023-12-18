

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt
from streamlit.hello.utils import show_code


generations = ["Lost Generation", "Greatest Generation", "Silent Generation", "Baby Boomers", 
                   "Generation X", "Millennials", "Generation Z", "Generation Alpha"]


def df_exploration():
    @st.cache_data
    def get_data():
        df = pd.read_csv('data/MS_prep.csv')
        return df

    try:
        movies_summary = get_data()
        
        st.title("Movie Trends Analysis")

        # Adding a selection box for generations
        selected_generation = st.selectbox("Select a Generation", generations)

        # Filtering based on the selected generation
        filtered_movies = movies_summary[movies_summary['Generation'] == selected_generation]

        # Plotting
        plt.figure(figsize=(12, 6))
        filtered_movies.groupby('Movie Release Year').size().plot(kind='line')
        plt.title(f'Trend of Movie Releases - {selected_generation}')
        plt.xlabel('Year')
        plt.ylabel('Number of Movies Released')
        plt.tight_layout()

        # Display in streamlit
        st.pyplot(plt)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


st.set_page_config(page_title="Data Exploration", page_icon="📊")
st.markdown("# Data Exploration")
st.sidebar.header("Data Exploration")


df_exploration()

