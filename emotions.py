import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

genres = ['Thriller', 'Romantic comedy', 'Horror', 'Short Film']
emotions_cols = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
generations = ["Lost Generation", "Greatest Generation", "Silent Generation", "Baby Boomers", 
                   "Generation X", "Millennials", "Generation Z", "Generation Alpha"]
default_colors = px.colors.qualitative.Plotly


## FERNANDO's PLOTS

## emotions along the plots (4 genres)
def emotions_along_time(movies_emotions, df_emotions):
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
    st.plotly_chart(fig, use_container_width=True)


## Heatmap of emotions
    
def format_emotions_data(movies_emotions, top_genres):
    cols = emotions_cols + ['Main Genre']
    heatmap_data = movies_emotions[cols]
    heatmap_data = heatmap_data[heatmap_data['Main Genre'].isin(top_genres)]

    return heatmap_data

def heatmap_emotions_genre(movies_emotions, top_genres):
    heatmap_data = format_emotions_data(movies_emotions, top_genres)

    # group by main genre & compute mean
    grouped_df = heatmap_data.groupby('Main Genre').mean().reset_index()
    long_df = grouped_df.melt('Main Genre', var_name='Emotion', value_name='Score')

    # drawing heatmap
    heatmap = alt.Chart(long_df).mark_rect().encode(
        x=alt.X('Emotion:N', title='Emotion'), y=alt.Y('Main Genre:N', title='Main Genre', sort=top_genres),
        color=alt.Color('Score:Q', scale=alt.Scale(scheme='spectral'), title='Score'),
        tooltip=['Main Genre', 'Emotion', 'Score']
    ).properties(width=alt.Step(40), height=600,
        title='Emotion scores by main genre')
    
    text = heatmap.mark_text(baseline='middle').encode(
        text=alt.Text('Score:Q', format='.2f'),
        color=alt.condition(
            alt.datum.Score > 4,
            alt.value('black'),  # light background
            alt.value('white')   # dark background
        )
    )

    st.altair_chart(heatmap + text, use_container_width=True)

## reduction & clustering
def emotion_clusters(movies_emotions, top_genres, method_name, df_reduced):
    cluster_data = format_emotions_data(movies_emotions, top_genres)

    cluster_data.dropna(inplace=True)
    df_reduced = df_reduced.join(cluster_data['Main Genre'])

    # plotting by actual movie genre
    fig1 = px.scatter(
        df_reduced,
        x=f'{method_name}1',
        y=f'{method_name}2',
        color='Main Genre',
        color_discrete_sequence=default_colors,
        title=f"Original Types - {method_name}",
        labels={'color': 'Main Genre'}
    )

    # plotting by identified K-means cluster
    fig2 = px.scatter(
        df_reduced,
        x=f'{method_name}1',
        y=f'{method_name}2',
        color='Labels',
        color_continuous_scale = default_colors,
        title=f"Discovered Clusters - {method_name}",
        labels={'color': 'Cluster Labels'}
    )

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)


def generation_emotions(movies_emotions):
    cols = emotions_cols + ['Generation']
    generation_emotions = movies_emotions[cols]
    generation_emotions = generation_emotions.groupby("Generation").mean().reset_index()

    all_generations_mean = generation_emotions[emotions_cols].mean().to_frame().T
    all_generations_mean['Generation'] = 'All Generations' 
    generation_emotions = pd.concat([generation_emotions, all_generations_mean], ignore_index=True)

    generation_emotions[emotions_cols] = generation_emotions[emotions_cols].div(generation_emotions[emotions_cols].sum(axis=1), axis=0) #normalize

    # keep order
    generation_emotions['Generation'] = pd.Categorical(generation_emotions['Generation'], categories=generations + ['All Generations'], ordered=True)
    generation_emotions = generation_emotions.sort_values('Generation')

    # stacked bar chart architecture
    generation_emotions_long = generation_emotions.melt('Generation', var_name='Emotion', value_name='Proportion')
    chart = alt.Chart(generation_emotions_long).mark_bar().encode(
        x=alt.X('Generation:N', title='Generation', sort=list(generation_emotions['Generation'].cat.categories), axis=alt.Axis(labelAngle=45)),
        y=alt.Y('sum(Proportion):Q', title='Proportion of emotions'),
        color='Emotion:N',
        order=alt.Order('Emotion:N', sort='ascending') 
    ).properties(title='Distribution of emotions across generations',
                 width=600,height=400)

    st.altair_chart(chart, use_container_width=True)

## XIAOCHENG's PLOTS
def regression_heatmap(df_params):    
    # if there's an 'Unnamed: 0' column due to indexing, drop it
    if 'Unnamed: 0' in df_params.columns:
        df_params.set_index('Unnamed: 0', inplace=True)
        df_params.index.name = 'Predictor'  # Rename the index to 'Predictor'

    # Melt the DataFrame to long format for Altair
    melted_df = df_params.reset_index().melt(id_vars='Predictor', var_name='Genre', value_name='Value')

    # heatmat architecture
    heatmap = alt.Chart(melted_df).mark_rect().encode(
        x=alt.X('Genre:N', title='Genre', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('Predictor:N', title='Predictor'),
        color=alt.Color('Value:Q', scale=alt.Scale(scheme='spectral')),
        tooltip=[
            alt.Tooltip('Predictor:N', title='Predictor'),
            alt.Tooltip('Genre:N', title='Genre'),
            alt.Tooltip('Value:Q', title='Value', format='.3f')
        ]
    ).properties(height=500, title="Heatmap of predictor by genre")

    # Create text labels for the heatmap
    text = heatmap.mark_text(baseline='middle').encode(
        text=alt.Text('Value:Q', format='.3f'),
        color=alt.condition(
            alt.datum.Value > 0,
            alt.value('black'),  # light background
            alt.value('white')   #dark background
        )
    )

    st.altair_chart(heatmap + text, use_container_width=True)


    
def sentiment_score_distribution(movies_summary):
    try:
        # histogram of sentiment scores
        chart = alt.Chart(movies_summary).mark_bar(opacity=0.7, color='skyblue').encode(
            alt.X('Sentiment score plot', bin=alt.Bin(maxbins=20), title='Sentiment score'),
            alt.Y('count()', title='Frequency')
        ).properties(width=600,height=400).interactive()

        # display chart 
        st.altair_chart(chart, use_container_width=True)
    except:
        st.error(
            """
            **An error has occured when plotting of this function. Please reload the page**
        """
        )