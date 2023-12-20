import streamlit as st
from streamlit.logger import get_logger
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import generations as gen
import emotions as emo

import streamlit as st

# --- CONFIG --- #

LOGGER = get_logger(__name__)

## --- IMAGES AND ANIMATIONS --- #
# movie_animation = load_animation("https://lottie.host/30a4816a-5b22-400d-92ab-30115ded0ab5/oh3wyo4dat.json")
# example_img = Image.open("images/example_img.JPG")
#st_lottie(movie_animation, speed=1, height=400, key="coding")
#st.image(example_img, caption="This is an example image", use_column_width=True)


# --- DATA --- #
def get_data(filename, index_col = False):
    if index_col:
        df = pd.read_csv('data/' + filename, index_col=0)
    else:     
        df = pd.read_csv('data/' + filename)
    df['Wikipedia Movie ID'] = pd.to_numeric(df['Wikipedia Movie ID'])    
    return df

def get_csv(filename):
    df = pd.read_csv('data/' + filename)  
    return df


movies_summary = get_data('movies_summary.csv')
emotions = get_data('MovieIDs_emotions.csv', index_col=True)
emotions_pca = get_csv('emotion_pca.csv')
emotions_tsne = get_csv('emotion_tsne.csv')
regression = get_csv('regression_params.csv')

filtered_movies = movies_summary.loc[movies_summary['Generation'] != 'Unknown Generation']
movies_emotions = emotions.merge(filtered_movies, on='Wikipedia Movie ID', how='left')
top_genres = movies_summary['Main Genre'].value_counts().head(10).index.tolist()

# --- PAGES --- #

def run():
    st.set_page_config(page_title="Feel the genres", page_icon=":sparkles:", layout="wide", initial_sidebar_state="collapsed")

    def load_animation(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # --- STYLE --- #

    def upload_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # --- HEADER --- #
    with st.container():
        st.title(":sparkles: Feel the genres :sparkles:, by Badafixm01")
        st.subheader("A data analysis story about movie genres and emotions")
        st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

    # --- SIDEBAR --- #
    with st.container():
        with st.sidebar:
            st.subheader("About the project")
            st.write("How can a movie genre achieve success in box office revenue? We primarily seek the answer in the realm of emotions. Film enthusiasts and casual viewers alike often base their movie choices on emotions they wish to experience, whether it is thrill, romance, fear, or joy. Utilising the movie plot summaries and their corresponding metadata, we could use NLP techniques to extract sentiment scores from these summaries. Our hypothesis is that certain sentiments, like joy or suspense, may consistently align with higher box office revenues for some genres. By correlating sentiment scores with box office revenues for different genres and potentially factoring in main character gender, release dates, countries and cultural contexts, this analysis aims to reveal the underlying emotional décor that drives moviegoers to the cinema. This investigation could not only provide valuable insights for film producers but also paint a picture of society's emotional needs and preferences at different times, across different countries.")
            st.subheader("Practical information")
            st.write("This project is a data analysis story about feeling genres emotions. Obviously guys, the website is not complete... With everyone working, I'm sure we'll get a hell of a grade.")
            st.write("The [data](https://www.cs.cmu.edu/~ark/personas/) was collected by David Bamman, Brendan O'Connor, and Noah Smith at the Language Technologies Institute and Machine Learning Department at Carnegie Mellon University, and the project is made with [Streamlit](https://streamlit.io/).")
            st.write("The project is hosted on [GitHub](https://ineskahlaoui.github.io/badafixm01/)")
            st.subheader("The team")
            st.write("[Inès Kahlaoui](https://www.linkedin.com/in/in%C3%A8s-kahlaoui-0862b71b8), [Mya Lahjouji](https://www.linkedin.com/in/mya-lahjouji-b05457233), [Berta Céspedes](https://www.linkedin.com/in/bertacespedes), Xiaocheng Zhang and [Fernando Meireles](https://www.linkedin.com/in/fernando-augusto-meireles-948a58157)")
            st.write("External libraries and frameworks used : ... to be completed ...")

    # --- DATA STORY --- #
            
    #### PART 1        
    with st.container():
        st.title("Part 1 : XX")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Column 1")
            st.write(""" 
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.""")
        with col2:
            st.header("Column 2")
            
        st.subheader("XXX")
        emo.emotions_along_time(movies_emotions, emotions)

        st.subheader("XXX")
        emo.heatmap_emotions_genre(movies_emotions, top_genres)

        st.subheader("XXX")
        emo.emotion_clusters(movies_emotions, top_genres, 'TSNE', emotions_tsne)

        st.subheader("XXX")
        emo.emotion_clusters(movies_emotions, top_genres, 'PCA', emotions_pca)

        st.subheader("XXX")
        emo.generation_emotions(movies_emotions)

        st.subheader("XXX")
        emo.regression_heatmap(regression)


    #### PART 2
    with st.container():
        st.title("Part 2 : XX")
        st.subheader("XXX")
        
        gen.plot_generations_movie_releases(movies_summary)

        st.subheader("XXX")
        gen.movie_count_per_generation(movies_summary)

        st.subheader("XXX")
        gen.genres_proportion(movies_summary)

        st.subheader("XXX")
        gen.genres_heatmap(filtered_movies, top_genres)

        st.subheader("XXX")
        gen.genres_proportion_per_generation(movies_summary, top_genres)

        st.subheader("XXX")
        gen.genre_proportion_for_generation(filtered_movies)


    # --- FOOTER --- #
    with st.container():
        st.title("Part 3 : XX")
        st.subheader("XXX")
        st.subheader("XXX")
        st.subheader("XXX")
     
        
if __name__ == "__main__":
    run()