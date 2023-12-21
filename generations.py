import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Setting up a color blind friendly pallete
CB_color_cycle = ['#377eb8','#ff7f00','#4daf4a',
                  '#f781bf','#a65628','#984ea3',
                  '#999999','#e41a1c','#dede00']

pastel_rainbow = ['#A1C9F4', '#FFB482', '#8DE5A1', '#FF9F9B', 
                  '#D0BBFF', '#DEBB9B', '#FAB0E4', '#CFCFCF']

generations_dict = {
    "Generation": ["Lost Generation", "Greatest Generation", "Silent Generation", "Baby Boomers", 
                   "Generation X", "Millennials", "Generation Z", "Generation Alpha"],
    "Start Year": [1883, 1901, 1928, 1946, 1965, 1981, 1997, 2010],
    "End Year": [1900, 1927, 1945, 1964, 1980, 1996, 2009, 2023]
}
generations = generations_dict['Generation']



df_generations = pd.DataFrame(generations_dict)

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


# Proportion of top 10 genres of whole dataset for each generation
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
    ).properties(width=700,height=400)

    st.altair_chart(chart, use_container_width=True)

# Proportion of top 10 genres of whole dataset for each generation - heatmap version
def genres_heatmap(movies_summary, top_genres):
    # Filter for top genres and calculate counts
    top_genre_data = movies_summary[movies_summary['Main Genre'].isin(top_genres)]

    # chronological order
    top_genre_data['Generation'] = pd.Categorical(top_genre_data['Generation'], 
                                                  categories=generations, ordered=True)
    
    genre_counts = top_genre_data.groupby(['Generation', 'Main Genre']).size().reset_index(name='Count')

    # Create the heatmap
    heatmap = alt.Chart(genre_counts).mark_rect().encode(
        x=alt.X('Main Genre:N', sort=top_genres),
        y=alt.Y('Generation:O', sort=generations),
        color=alt.Color('Count:Q', scale=alt.Scale(scheme='spectral')),
        tooltip=['Generation', 'Main Genre', 'Count']
    ).properties(
        width=alt.Step(40), 
        height=600,
        title="Heatmap of Top Genres per Generation"
    )

    text = heatmap.mark_text(baseline='middle').encode(
        text=alt.Text('Count:Q'),
        color=alt.condition(
            alt.datum.Count > 950,
            alt.value('black'),  # light background
            alt.value('white')   # dark background
        )
    )

    st.altair_chart(heatmap + text, use_container_width=True) 

def genre_porportion_for_generation(movies_summary):
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


def genre_proportion_for_generation(movies_summary_gen):
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
    top_genres_per_generation['Generation'] = pd.Categorical(
        top_genres_per_generation['Generation'], categories=generations, ordered=True)

    # parallel  diagram
    fig = px.parallel_categories(top_genres_per_generation, 
                                 dimensions=['Generation', 'Main Genre'], color='Count', 
                                 color_continuous_scale='spectral')

    # Adjust figure size
    fig.update_layout(margin=dict(l=100),  # avoid text cutting
                      width=900, height=900)

    st.plotly_chart(fig, use_container_width=True)


## number of movies released per generation
## average sentiment score per generation