import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import colorsys


default_colors = px.colors.qualitative.Plotly

## Number of movies per generation
def movie_count_per_generation(movies_summary, generations):
    movies_per_generation = movies_summary['Generation'].value_counts().reindex(generations).fillna(0).reset_index()
    movies_per_generation.columns = ['Generation', 'Number of Movies']

    # bar chart
    chart = alt.Chart(movies_per_generation).mark_bar(color='#1bd3f3').encode(
        x=alt.X('Generation', sort=None, axis=alt.Axis(labelAngle=-60)),  
        y='Number of Movies',
        tooltip=['Generation', 'Number of Movies']
    ).properties(
        width=700,
        height=400, title = 'Number of movie released per generation'
    )

    # display chart
    st.altair_chart(chart, use_container_width=True)

## Proportion of genres per generation 
def genres_proportion(movies_summary, generations):
    genre_counts = movies_summary['Main Genre'].value_counts().nlargest(10)
    genre_df = pd.DataFrame({'Main Genre': genre_counts.index, 'Count': genre_counts.values})

    # compute percentage
    genre_df['Percentage'] = (genre_df['Count'] / genre_df['Count'].sum() * 100).round(2)

    # create pie chart architecture
    fig = px.pie(genre_df, names='Main Genre', values='Percentage',
                 hover_data=['Main Genre'], labels={'Main Genre':'Genre'}, color_discrete_sequence = default_colors)
    
    # display percentages on chart and pull slices out
    fig.update_traces(textinfo='percent+label', pull=[0.1] * genre_df.shape[0])
    fig.update_layout(title='Top 10 movie main genres proportion')

    # display chart
    st.plotly_chart(fig, use_container_width=True)


# Proportion of top 10 genres of whole dataset for each generation
def genres_proportion_per_generation(movies_summary, top_genres, generations):
    # include only the top genres
    movies_top_genres = movies_summary[movies_summary['Main Genre'].isin(top_genres)].copy()
    movies_top_genres['Generation'] = pd.Categorical(movies_top_genres['Generation'], categories=generations, ordered=True)

    # occurrences of top genres within each generation
    genre_by_generation = pd.crosstab(movies_top_genres['Generation'], movies_top_genres['Main Genre'])
    genre_by_generation = genre_by_generation.reindex(generations)
    genre_by_generation_normalized = genre_by_generation.div(genre_by_generation.sum(axis=1), axis=0)

    # compute proportions for all generations
    overall_proportions = genre_by_generation.sum(axis=0) / genre_by_generation.sum().sum()
    overall_proportions = pd.DataFrame(overall_proportions).transpose()
    overall_proportions.index = ['All Generations']

    genre_by_generation_normalized = pd.concat([genre_by_generation_normalized, overall_proportions])
    genre_by_generation_normalized = genre_by_generation_normalized.reset_index()
    genre_by_generation_normalized['index'] = pd.Categorical(genre_by_generation_normalized['index'], categories=generations + ['All Generations'], ordered=True)

    # stacked bar chart architecture
    data_long = genre_by_generation_normalized.melt('index', var_name='Genre', value_name='Proportion')

    domain = top_genres
    range_ = default_colors[:len(domain)]

    chart = alt.Chart(data_long).mark_bar().encode(
        x=alt.X('index:N', sort=generations + ['All Generations']),  # Explicitly sort the x-axis
        y=alt.Y('Proportion:Q', stack='normalize'),
        color=alt.Color('Genre:N', scale=alt.Scale(domain=domain, range=range_)),
        tooltip=['index', 'Genre', alt.Tooltip('Proportion:Q', format='.1%')]
    ).properties(width=700,height=500, title = 'Number of movies by top 10 main genres in the dataset across generations')

    st.altair_chart(chart, use_container_width=True)

# Proportion of top 10 genres of whole dataset for each generation - heatmap version
def genres_heatmap(movies_summary, top_genres, generations):
    # Filter for top genres and calculate counts
    top_genre_data = movies_summary[movies_summary['Main Genre'].isin(top_genres)].copy()

    # chronological order
    top_genre_data['Generation'] = pd.Categorical(top_genre_data['Generation'], categories=generations, ordered=True)
    genre_counts = top_genre_data.groupby(['Generation', 'Main Genre'], observed = True).size().reset_index(name='Count')

    # heatmap architecture
    rainbow_colors = sorted(default_colors, key=lambda rgb: colorsys.rgb_to_hsv(*[int(rgb.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)]))

    heatmap = alt.Chart(genre_counts).mark_rect().encode(
        x=alt.X('Main Genre:N', sort=top_genres),
        y=alt.Y('Generation:O', sort=generations),
        color=alt.Color('Count:Q', scale=alt.Scale(range=rainbow_colors)),
        tooltip=['Generation', 'Main Genre', 'Count']
    ).properties(
        width=alt.Step(40), 
        height=600, title = 'Number of movies by top 10 main genres in the dataset across generations'
    )

    text = heatmap.mark_text(baseline='middle').encode(
        text=alt.Text('Count:Q'),
        color=alt.condition(
            alt.datum.Count > 950,
            alt.value('black'),  # light background
            alt.value('white')   # dark background
        ))

    st.altair_chart(heatmap + text, use_container_width=True) 

def genre_porportion_for_generation(movies_summary, generations):
    # count of movies per genre for each generation
    genre_counts_per_generation = (
        movies_summary.groupby(['Generation', 'Main Genre'])
        .size()
        .reset_index(name='Count')
        .sort_values(['Generation', 'Count'], ascending=[True, False])
    )

    # top genres for each generation
    top_genres_per_generation = genre_counts_per_generation.groupby('Generation').head(10)

    # individual charts for each generation
    charts = []
    for generation in generations:
        generation_data = top_genres_per_generation[top_genres_per_generation['Generation'] == generation]
        chart = alt.Chart(generation_data).mark_bar().encode(
            x=alt.X('Main Genre', sort='-y'),
            y='Count',
            color='Main Genre',
            tooltip=['Main Genre', 'Count']
        ).properties(
            title=f'Top Genres for {generation}',
            width=300,
            height=200
        )
        charts.append(chart)

    # combine into grid layout
    combined_chart = alt.vconcat(*[alt.hconcat(*charts[i:i+3]) for i in range(0, len(charts), 3)])

    st.altair_chart(combined_chart, use_container_width=True)


def genre_proportion_for_generation(movies_summary_gen, generations):

    # remove generation alpha as not relevant in the analysis
    movies_summary_gen = movies_summary_gen[movies_summary_gen['Generation'] != 'Generation Alpha'].copy()
    # compute top 10 genres for each generation separately
    top_genres_per_generation = (
        movies_summary_gen.groupby(['Generation', 'Main Genre'])
        .size()
        .reset_index(name='Count')
        .groupby('Generation')
        .apply(lambda x: x.nlargest(10, 'Count'))
        .reset_index(drop=True)
    )

    # ensure generations are in chronological order
    top_genres_per_generation['Generation'] = pd.Categorical(top_genres_per_generation['Generation'], categories=generations, ordered=True)
    top_genres_per_generation.sort_values(by='Generation', inplace=True)

    # parallel  diagram
    # manually pre-computed percentiles
    color_scale = [[0, '#636EFA'],[0.009, '#19D3F3'],[0.051, '#00CC96'],[0.065, '#B6E880'],[0.080, '#FFA15A'],[0.092, '#FECB52'],
                   [0.109, '#FF6692'],[0.175, '#FF97FF'],[0.225, '#EF553B'],[1, '#AB63FA']]
    genre_order = (top_genres_per_generation.groupby('Main Genre', observed = True)['Count'].sum().sort_values(ascending=False).index.tolist())
    fig = px.parallel_categories(top_genres_per_generation, 
                                 dimensions=['Generation', 'Main Genre'], color='Count', 
                                 color_continuous_scale=color_scale)

    
    # Adjust figure size
    fig.update_layout(margin=dict(l=100),  # avoid text cutting
                      width=900, height=900, title = 'Number of movies by top 10 main genres for each generation across generations')

    st.plotly_chart(fig, use_container_width=True)

