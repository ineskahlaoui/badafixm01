from urllib.error import URLError

import altair as alt
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st



## Movie releases by year (filtered with generations)
def plot_generations_movie_releases(movies_summary):
    try:
        generations = ["Lost Generation", "Greatest Generation", "Silent Generation", "Baby Boomers", 
                   "Generation X", "Millennials", "Generation Z", "Generation Alpha"]
        
        # adding multi-select box for generations
        selected_generations = st.multiselect("Select Generations", generations, default=generations)

        if not selected_generations:
            st.error("Please select at least one generation.")
        else:
            # filtering data based on the selected generations
            filtered_movies = movies_summary[movies_summary['Generation'].isin(selected_generations)]

            # preparing data for chart
            yearly_data = filtered_movies.groupby(['Movie Release Year', 'Generation']).size().reset_index(name='Number of Movies')
            chart = alt.Chart(yearly_data).mark_line().encode(
                x='Movie Release Year',
                y='Number of Movies',
                color='Generation',
                tooltip=['Movie Release Year', 'Number of Movies', 'Generation']
            ).interactive()

            # display altair chart
            st.altair_chart(chart, use_container_width=True)
    except:
        st.error(
            """
            **An error has occured within the plotting of this function.**
        """
        )


def sentiment_score_distribution(movies_summary):
    try:
        # histogram of sentiment scores
        chart = alt.Chart(movies_summary).mark_bar(opacity=0.7, color='skyblue').encode(
            alt.X('Sentiment score plot', bin=alt.Bin(maxbins=20), title='Sentiment Score'),
            alt.Y('count()', title='Frequency')
        ).properties(
            width=600,
            height=400
        ).interactive()

        # display chart 
        st.altair_chart(chart, use_container_width=True)
    except:
        st.error(
            """
            **An error has occured within the plotting of this function.**
        """
        )