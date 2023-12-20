import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

genres = ['Thriller', 'Romantic comedy', 'Horror', 'Short Film']

## FERNANDO's PLOTS
def emotions_along_time(movies_summary, df_emotions):
    movies_emotions = df_emotions.merge(movies_summary, on='Wikipedia Movie ID', how='left')
    movies_emotions_norm = movies_emotions.copy()
    Total_score = movies_emotions_norm[movies_emotions_norm.columns[1:9]].sum(axis=1).copy()
    for i in range(1,9):
        movies_emotions_norm[movies_emotions_norm.columns[i]] = movies_emotions_norm[movies_emotions_norm.columns[i]]*100/Total_score

    # select emotions to display
    emotions = df_emotions.columns[1:9].tolist()
    selected_emotions = st.multiselect('Select emotions to display:', emotions, default=emotions)
    color_map = {emotion: color for emotion, color in zip(emotions, px.colors.qualitative.Plotly)}

    # 2x2 grid
    fig = make_subplots(rows=2, cols=2, subplot_titles=genres, shared_yaxes=True)

    # create traces for each emotion
    first_trace_legend = {emotion: True for emotion in emotions}
    for i, genre in enumerate(genres):
        row = (i // 2) + 1
        col = (i % 2) + 1
        genre_data = movies_emotions_norm[movies_emotions_norm["Main Genre"] == genre]
        genre_data_sorted = genre_data.sort_values(by="Movie Release Year")

        for emotion in selected_emotions:
            show_in_legend = first_trace_legend.get(emotion, False)
            
            first_trace_legend[emotion] = False
            genre_data_non_zero = genre_data_sorted[genre_data_sorted[emotion] != 0]
            fig.add_trace(go.Scatter(
                x=genre_data_non_zero["Movie Release Year"],y=genre_data_non_zero[emotion],
                name=emotion,
                line=dict(color=color_map[emotion]),connectgaps=True,
                showlegend=show_in_legend
            ), row=row, col=col)

    # Unified legend
    fig.update_layout(height=800,width=1000,
        title_text="Emotion intensity scores by genre over time",
        legend_title="Emotions",
        legend=dict(traceorder='normal',font=dict(size=10),itemsizing='constant'),
        showlegend=True)

    # display plot
    for trace in fig.data:
        trace.visible = trace.name in selected_emotions
    st.plotly_chart(fig, use_container_width=False)



## XIAOCHENG's PLOTS

def sentiment_score_distribution(movies_summary):
    try:
        # histogram of sentiment scores
        chart = alt.Chart(movies_summary).mark_bar(opacity=0.7, color='skyblue').encode(
            alt.X('Sentiment score plot', bin=alt.Bin(maxbins=20), title='Sentiment score'),
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