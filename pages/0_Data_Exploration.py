

from urllib.error import URLError

import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import generations as gen
import emotions as emo

import streamlit as st

from streamlit.hello.utils import show_code

st.set_page_config(page_title="Data Exploration", page_icon="📊")
st.markdown("# Data Exploration")
st.sidebar.header("Data Exploration")

@st.cache_data
def get_data(filename, index_col = False):
    if index_col:
        df = pd.read_csv('data/' + filename, index_col=0)
    else:     
        df = pd.read_csv('data/' + filename)
    df['Wikipedia Movie ID'] = pd.to_numeric(df['Wikipedia Movie ID'])    
    return df

movies_summary = get_data('movies_summary.csv')
emotions = get_data('MovieIDs_emotions.csv', index_col=True)

filtered_movies = movies_summary.loc[movies_summary['Generation'] != 'Unknown Generation']
top_genres = movies_summary['Main Genre'].value_counts().head(10).index.tolist()


###### 1 ######
emo.emotions_along_time(movies_summary, emotions)


###### 2 ######
st.title("Movie Trends Analysis")
st.write(""" The social norms and values of each generation are shaped by historical events, cultural developments, technological advances, and other societal changes.
         """)


gen.plot_generations_movie_releases(movies_summary)

st.title("Movie Trends by Generation")
gen.movie_count_per_generation(movies_summary)


gen.genres_proportion(movies_summary)

gen.genres_heatmap(filtered_movies, top_genres)

gen.genres_proportion_per_generation(movies_summary, top_genres)

# gen.genre_porportion_for_generation(filtered_movies)

gen.genre_proportion_for_generation(filtered_movies)

## ADD IN PART 1
# st.title("Sentiment score")
# gen.sentiment_score_distribution(movies_summary)

