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
import historical_events as hist
import texts

# --- CONFIG --- #

LOGGER = get_logger(__name__)

def set_css():
        css = """
        <style>
            /* Main page layout */
            .main .block-container {
                padding-right: 12rem;   
                padding-left: 12rem;    
            }
            .justified-text {
                text-align: justify;
                text-justify: inter-word;
            }
            .size-text { font-size: 18px; }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

def load_animation(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

## --- IMAGES AND ANIMATIONS --- #
movie_animation = load_animation("https://lottie.host/30a4816a-5b22-400d-92ab-30115ded0ab5/oh3wyo4dat.json")
# example_img = Image.open("images/example_img.JPG")
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
word_clouds = get_csv('word_cloud.csv')

filtered_movies = movies_summary.loc[movies_summary['Generation'] != 'Unknown Generation']
movies_emotions = emotions.merge(filtered_movies, on='Wikipedia Movie ID', how='left')
top_genres = movies_summary['Main Genre'].value_counts().head(10).index.tolist()

generations_dict = {
    "Generation": ["Lost Generation", "Greatest Generation", "Silent Generation", "Baby Boomers", 
                   "Generation X", "Millennials", "Generation Z", "Generation Alpha"],
    "Start Year": [1883, 1901, 1928, 1946, 1965, 1981, 1997, 2010],
    "End Year": [1900, 1927, 1945, 1964, 1980, 1996, 2009, 2023]
}
generations = generations_dict['Generation']
df_generations = pd.DataFrame(generations_dict)

# --- PAGES --- #

def run():
    st.set_page_config(page_title="Feel the genres", page_icon=":sparkles:", layout="wide", initial_sidebar_state="collapsed")

    # if needed
    def upload_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    set_css()

    # --- HEADER --- #
    with st.container():
        st.title(":sparkles: Let's find a new title lol :sparkles:")
        st.subheader("Introduction")
        col1, col2 = st.columns(2)
        with col1:
            texts.introduction()
        with col2:
            st_lottie(movie_animation, speed=1, height=400, key="coding")

        

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
            
    #### PART 1 ####
    with st.container():
        st.title("A backstory about generations and genres")

        texts.generations_explained()

        texts.movies_released_per_generation()
        gen.movie_count_per_generation(movies_summary, generations)
        texts.movies_released_analysis()

        st.subheader("A closer look at movie preferences throughout time thanks to genres")
        texts.pie_introduction()
        gen.genres_proportion(movies_summary, generations)
        texts.pie_analysis()

        gen.genres_heatmap(filtered_movies, top_genres, generations)
        texts.heatmap_analysis()

        gen.genres_proportion_per_generation(movies_summary, top_genres, generations)
        texts.stacked_genres_analysis()

        texts.parallel_genres_intro()
        gen.genre_proportion_for_generation(filtered_movies, generations)
        texts.parallel_genres_analysis()
            
    #### PART 2 ####       
    with st.container():
        st.title("When emotions come into play")
        texts.emotion_dataset()   

        st.subheader("Emotions over the years")
        texts.emotion_lines_intro()
        emo.emotions_along_time(movies_emotions, emotions)
        texts.emotion_lines()

        emo.heatmap_emotions_genre(movies_emotions, top_genres)
        texts.emotion_heatmap()

        texts.emotion_clusters_intro()
        emo.emotion_clusters(movies_emotions, top_genres, 'TSNE', emotions_tsne)
        emo.emotion_clusters(movies_emotions, top_genres, 'PCA', emotions_pca)
        texts.emotion_clusters()

        st.subheader("Emotions shaping genres")
        texts.regression_intro()
        emo.regression_heatmap(regression)
        texts.regression()
        texts.regression_findings()


        st.subheader("What about emotions across generations?")
        texts.emotion_generations_intro()
        emo.generation_emotions(movies_emotions)
        texts.emotion_generations()
        
    #### PART 3 ####   
    with st.container():
        st.title("Part 3 : put Berta after these plots")
        st.subheader("XXX")
        
        hist.plot_generations_movie_releases(movies_summary, generations)
        st.subheader("XXX")
        hist.generations_movie_releases_countries(movies_summary, generations)

        st.subheader("XXX")
        hist.wordcloud(word_clouds)
        st.subheader("XXX")
        st.subheader("XXX")
     
        
if __name__ == "__main__":
    run()