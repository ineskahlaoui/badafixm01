from urllib.error import URLError

import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


generations_dict = {
    "Generation": ["Lost Generation", "Greatest Generation", "Silent Generation", "Baby Boomers", 
                   "Generation X", "Millennials", "Generation Z", "Generation Alpha"],
    "Start Year": [1883, 1901, 1928, 1946, 1965, 1981, 1997, 2010],
    "End Year": [1900, 1927, 1945, 1964, 1980, 1996, 2009, 2023]
}
generations = generations_dict['Generation']

df_generations = pd.DataFrame(generations_dict)


#### 1 ####
## Movie releases by year (filtered with generations)
def plot_generations_movie_releases(movies_summary):
    try:
        
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


#### 2 ####
## Number of movies per generation
def movie_count_per_generation(movies_summary):
    movies_per_generation = movies_summary['Generation'].value_counts().reindex(generations).fillna(0).reset_index()
    movies_per_generation.columns = ['Generation', 'Number of Movies']

    # bar chart
    chart = alt.Chart(movies_per_generation).mark_bar(color='skyblue').encode(
        x=alt.X('Generation', sort=None, axis=alt.Axis(labelAngle=-60)),  
        y='Number of Movies',
        tooltip=['Generation', 'Number of Movies']
    ).properties(
        width=700,
        height=400
    )

    # display chart
    st.altair_chart(chart, use_container_width=True)


## Proportion of genres per generation 
def genres_proportion(movies_summary):
    genre_counts = movies_summary['Main Genre'].value_counts().nlargest(10)
    genre_df = pd.DataFrame({'Main Genre': genre_counts.index, 'Count': genre_counts.values})

    # compute percentage
    genre_df['Percentage'] = (genre_df['Count'] / genre_df['Count'].sum() * 100).round(2)

    # create pie chart architecture
    fig = px.pie(genre_df, names='Main Genre', values='Percentage',
                 title='Top 10 Movie Main Genres Distribution', ## REMOVE TITLE AFTERWARDS
                 hover_data=['Main Genre'], labels={'Main Genre':'Genre'})
    
    # display percentages on chart and pull slices out
    fig.update_traces(textinfo='percent+label', pull=[0.1] * genre_df.shape[0])

    # display chart
    st.plotly_chart(fig, use_container_width=True)


def genres_proportion_per_generation(movies_summary, top_genres):
    # include only the top genres
    movies_top_genres = movies_summary[movies_summary['Main Genre'].isin(top_genres)]
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
    chart = alt.Chart(data_long).mark_bar().encode(
        x=alt.X('index:N', sort=generations + ['All Generations']),  # Explicitly sort the x-axis
        y=alt.Y('Proportion:Q', stack='normalize'),
        color='Genre:N',
        tooltip=['index', 'Genre', alt.Tooltip('Proportion:Q', format='.1%')]
    ).properties(
        width=700,
        height=400
    )

    # display chart
    st.altair_chart(chart, use_container_width=True)





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


