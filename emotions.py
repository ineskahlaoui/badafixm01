import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



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