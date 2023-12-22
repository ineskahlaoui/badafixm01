import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import colorsys
from collections import Counter

# define periods
periods = [
            {"start": 1914, "end": 1918, "event": "WW1", "color": "lightgrey"},
            {"start": 1939, "end": 1945, "event": "WW2", "color": "lightgrey"},
            {"start": 1929, "end": 1939, "event": "Great Depression", "color": "lightblue"},
            {"start": 2007, "end": 2009, "event": "Global Financial Crisis", "color": "lightgreen"}
        ]


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


## movie distribution per top 5 countries
def generations_movie_releases_countries(movies_summary, generations):
    movies_summary = movies_summary[movies_summary['Movie Countries'].apply(lambda x: x != [''])]
    top_countries = movies_summary['Movie Countries'].value_counts().head(6).index.tolist()
    filtered_movies = movies_summary[movies_summary['Movie Countries'].isin(top_countries)]

    selected_generations = st.multiselect("Select Generations ok", generations, default=generations)

    if not selected_generations:
        st.error("Please select at least one generation.")
    else:
        # filtering data based on the selected generations
        filtered_movies = filtered_movies[filtered_movies['Generation'].isin(selected_generations)]
        yearly_data = filtered_movies.groupby(['Movie Release Year', 'Movie Countries']).size().reset_index(name='Number of Movies')
        
        # base chart for the lines
        line_chart = alt.Chart(yearly_data).mark_line().encode(
                x='Movie Release Year:O',
                y='Number of Movies:Q',
                color='Movie Countries:N',  # Update to 'Movie Countries'
                tooltip=['Movie Release Year', 'Number of Movies', 'Movie Countries']  # Update tooltip
            )

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
        


## wordcloud of movie summaries
def wordcloud(word_cloud):
    emotions_list = [ emotion.strip() for sublist in word_cloud.iloc[:, 0].dropna().astype(str).str.split(',')
        for emotion in sublist if isinstance(emotion, str) and emotion.strip()
    ]

    # Recalculate the frequency of each unique emotion
    frequencies = Counter(emotions_list)

    # Display the most common emotions and their counts
    frequencies.most_common(10)


    positions = {word: (np.random.rand(), np.random.rand()) for word in frequencies}

    # Create a scatter plot
    trace = go.Scatter(
        x=[pos[0] for pos in positions.values()],
        y=[pos[1] for pos in positions.values()],
        text=list(frequencies.keys()),
        mode='text',
        textfont={'size': [np.sqrt(frequencies[word]) * 10 for word in frequencies.keys()], 'color': 'black'},
    )

    # Define layout with no axis and white background
    layout = go.Layout(
        xaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False},
        yaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False},
        plot_bgcolor='white',
        margin={'l': 0, 'r': 0, 't': 0, 'b': 0}
    )

    # Create and show the figure
    fig = go.Figure(data=[trace], layout=layout)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)