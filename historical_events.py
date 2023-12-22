import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from collections import Counter
import ast

default_colors = px.colors.qualitative.Plotly

# define periods
periods = [
            {"start": 1939, "end": 1945, "event": "WW2", "color": "lightgrey"},
            {"start": 1945, "end": 1991, "event": "Cold War", "color": "lightblue"},
            {"start": 2001, "end": 2002, "event": "9/11", "color": "lightgreen"}
        ]


## Movie releases by year (filtered with generations)
def plot_generations_movie_releases(movies_sum, generations):
    movies_summary = movies_sum.copy()
    movies_summary = movies_summary[movies_summary['Movie Release Year'] < 2013]
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
def generations_movie_releases_countries(movies_sum, generations):
    movies_summary = movies_sum.copy()
    movies_summary = movies_summary[movies_summary['Movie Release Year'] < 2013]
    movies_summary['Movie Countries'] = movies_summary['Movie Countries'].apply(ast.literal_eval)
    
    movies_summary['Movie Country'] = movies_summary['Movie Countries'].apply(lambda x: x[0] if x else None)
    movies_summary = movies_summary[movies_summary['Movie Country'] != '']
    top_countries = movies_summary['Movie Country'].value_counts().head(5).index.tolist()
    
    filtered_movies = movies_summary[movies_summary['Movie Country'].isin(top_countries)]

    selected_generations = st.multiselect("Please select generations", generations, default=generations)

    if not selected_generations:
        st.error("Please select at least one generation.")
    else:
        # filtering data based on the selected generations
        filtered_movies = filtered_movies[filtered_movies['Generation'].isin(selected_generations)]
        yearly_data = filtered_movies.groupby(['Movie Release Year', 'Movie Country']).size().reset_index(name='Number of Movies')
        
        # base chart for the lines
        line_chart = alt.Chart(yearly_data).mark_line().encode(
                x='Movie Release Year:O',
                y='Number of Movies:Q',
                color='Movie Country:N',  # Update to 'Movie Countries'
                tooltip=['Movie Release Year', 'Number of Movies', 'Movie Country']  # Update tooltip
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
def wordcloud(freq):

    year_ranges = [[1947, 1952], [1980, 1985], [2003, 2008], [1996, 2001]]
    periods = ['Post World War 2', 'Post Cold War', 'Post 9/11', 'a control period']

    for year_range, period in zip(year_ranges, periods):
        wc = freq[(freq['date'] >= year_range[0]) & (freq['date'] <= year_range[1])]
        summed_frequencies = wc.drop('date', axis=1).sum().to_dict()
        words = list(summed_frequencies.keys())
        frequencies = list(summed_frequencies.values())
        
        # assign a color to each word
        word_colors = [default_colors[i % len(default_colors)] for i in range(len(words))]
        sizes = [np.log(v+1)*10 for v in frequencies]  # log to reduce range of sizes
        x_positions = np.random.rand(len(words))  
        y_positions = np.random.rand(len(words))  

        # scatter plot
        trace = go.Scatter(
            x=x_positions,
            y=y_positions,
            text=words,
            mode='text',
            textfont={'size': sizes, 'color': word_colors},
            hoverinfo='text'
        )

        layout = go.Layout(
            title=f"Emotion word cloud for {period} ({year_range[0]}-{year_range[1]})",
            xaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False},
            yaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False}
        )

        fig = go.Figure(data=[trace], layout=layout)
        st.plotly_chart(fig, use_container_width=True)


def world_map(ISO_movie_counts):
    percentiles = np.percentile(ISO_movie_counts['Movie count'], [10, 20, 30, 40, 50, 60, 70, 80, 90])
    max = ISO_movie_counts['Movie count'].max()
    color_scale = [
        [0, '#fecb51'],  # yellow
        [percentiles[1]/max, '#ffa15a'],  # plotly orange
        [percentiles[3]/max, '#ef553b'],  # plotly red
        [percentiles[4]/max, '#faeae1'],  # White
        [percentiles[8]/max, '#ab63fa'],  # plotly purple
        [1, '#636efa']   # plotly dark blue
        ]
    # choropleth map
    fig = px.choropleth(ISO_movie_counts, 
                        locations='ISO alpha', 
                        color='Movie count', 
                        hover_name='Country', 
                        color_continuous_scale=color_scale)

    # Update layout
    fig.update_layout(
        title_text='Global amount of movies distribution',
        title_x=0.5,
        title_font=dict(size=24),
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='natural earth'
        ),
        width=700,  height=600)

    # Show the plot
    st.plotly_chart(fig, use_container_width=True)