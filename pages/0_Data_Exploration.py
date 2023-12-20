

from urllib.error import URLError

import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import exploration_plots as exp

import streamlit as st

from streamlit.hello.utils import show_code

st.set_page_config(page_title="Data Exploration", page_icon="📊")
st.markdown("# Data Exploration")
st.sidebar.header("Data Exploration")

@st.cache_data
def get_data():
    df = pd.read_csv('data/MS_prep.csv')
    return df

movies_summary = get_data()
top_genres = movies_summary['Main Genre'].value_counts().head(10).index.tolist()

generations_info = {
    "Lost Generation (born approximately 1883–1900)": [
        "This generation came of age during World War I and the Roaring Twenties.",
        "They were often characterized by a sense of disillusionment with war.",
        "There was a notable shift toward modernist art and literature."
    ],
    "Greatest Generation (born approximately 1901–1927)": [
        "They lived through the Great Depression, which instilled values of frugality and a strong work ethic.",
        "Many served in World War II, leading to a strong sense of duty and sacrifice.",
        "They valued community cohesion and respect for authority."
    ],
    "Silent Generation (born approximately 1928–1945)": [
        "Grew up during economic depression and war but came of age during the post-war boom.",
        "They are often seen as conformist and civic-minded.",
        "A value for stability, hard work, and keeping quiet about one’s troubles was prevalent."
    ],
    "Baby Boomers (born approximately 1946–1964)": [
        "Came of age during the civil rights movement, Vietnam War, and the Sexual Revolution.",
        "They often challenged established social norms and authority.",
        "Values included individualism, equal rights, and personal freedom."
    ],
    "Generation X (born approximately 1965–1980)": [
        "Grew up during a time of economic uncertainty and the rise of divorce rates.",
        "Often values independence, resilience, and a balance between work and personal life.",
        "This generation is sometimes seen as skeptical and value-driven."
    ],
    "Millennials (born approximately 1981–1996)": [
        "Came of age during the internet boom, which influenced their values towards connectivity and innovation.",
        "They tend to value diversity, equality, and sustainability.",
        "Known for valuing experiences over material possessions."
    ],
    "Generation Z (born approximately 1997–2009)": [
        "They are digital natives who value inclusivity, individuality, and authenticity.",
        "Grew up during the global recession and are thus thought to be pragmatic and financially minded.",
        "Social justice and environmental concerns are significant for this group."
    ],
    "Generation Alpha (born approximately 2010–2024)": [
        "It's too early to fully define the norms and values of this generation.",
        "They are being raised in an era of advanced technology and artificial intelligence.",
        "Early indications suggest they will value digital literacy, mental health, and environmental issues."
    ]
}


###### 2 ######
st.title("Movie Trends Analysis")
st.write(""" The social norms and values of each generation are shaped by historical events, cultural developments, technological advances, and other societal changes.
         """)

for generation, characteristics in generations_info.items():
    st.subheader(generation)
    for char in characteristics:
        st.write("- " + char)


exp.plot_generations_movie_releases(movies_summary)

st.title("Movie Trends by Generation")
exp.movie_count_per_generation(movies_summary)


exp.genres_proportion(movies_summary)

exp.genres_proportion_per_generation(movies_summary, top_genres)

st.title("Sentiment score")
exp.sentiment_score_distribution(movies_summary)

