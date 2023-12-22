import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import colorsys


## Movie releases by year (filtered with generations)
def plot_generations_movie_releases(movies_summary, generations):
    selected_generations = st.multiselect("Select Generations", generations, default=generations)

    if not selected_generations:
        st.error("Please select at least one generation.")
    else:
        # filtering data based on the selected generations
        filtered_movies = movies_summary[movies_summary['Generation'].isin(selected_generations)]
        yearly_data = filtered_movies.groupby(['Movie Release Year', 'Generation']).size().reset_index(name='Number of Movies')
        
        # base chart for the lines
        line_chart = alt.Chart(yearly_data).mark_line().encode(
                x='Movie Release Year:O',
                y='Number of Movies:Q',
                color='Generation:N',
                tooltip=['Movie Release Year', 'Number of Movies', 'Generation']
            )

        # define periods
        periods = [
            {"start": 1914, "end": 1918, "event": "WW1", "color": "lightgrey"},
            {"start": 1939, "end": 1945, "event": "WW2", "color": "lightgrey"},
            {"start": 1929, "end": 1939, "event": "Great Depression", "color": "lightblue"},
            {"start": 2007, "end": 2009, "event": "Global Financial Crisis", "color": "lightgreen"}
        ]

        # shaded areas & corresponding labels for period
        layers = [line_chart]
        for p in periods:
            area = alt.Chart(alt.Data(values=[{'start': p['start'], 'end': p['end']}])).mark_rect(
                opacity=0.5, color=p['color']).encode(
                x='start:O',
                x2='end:O'
            )

            text = alt.Chart(alt.Data(values=[{'start': p['start'], 'event': p['event']}])).mark_text(
                align='left', baseline='top', dx=5, dy=-5, color=p['color']).encode(
                x='start:O',
                text='event:N'
            )

            layers.append(area)
            layers.append(text)

        # Combine all layers into a single chart
        chart = alt.layer(*layers).resolve_scale(x='shared').interactive()
        st.altair_chart(chart, use_container_width=True)
