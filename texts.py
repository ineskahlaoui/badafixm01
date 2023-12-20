import streamlit as st


def regression():
    st.subheader("Methodology")

    # Description of the methodology
    st.markdown("""
    An Ordinary Least Squares model was constructed for each genre using sentiment scores and the intensities of eight emotions as predictors. 
                The data underwent paired matching on countries, languages, generation, and runtime to mitigate the effect of confounding factors. 
                The heatmap displays the slopes of linear regressions between one-hot encoded genres and emotion intensities and sentiment score of movie plot summaries.
                 All visualized slopes are statistically significant \(p < 0.05\). 
                The slopes indicate the degree that an emotion or sentiment shapes the likelihood that a movie belongs to a genre. 
                Indeed, there are interesting patterns of emotional influence in some genres:
    """)

    st.subheader("Key Findings")

    st.markdown("""
    -   **Tension in Thriller:** The `Thriller` genre show the strongest association with emotions. 
                Notably, `fear` and `joy` exhibit a positive and negative correlations with the probability of this genre, respectively, suggesting a generally negative emotional tone. 
                This observation aligns with the genre's weakly negative relationship with the sentiment score. 
    -   **Light Mood in Romantic Comedy:** In contrast, the `Romantic Comedy` genre shows opposite trends in its relationship with `fear`, `joy`, 
                and sentiment score compared to `Thriller`. These trends indicate a light mood within the genre.
    -   **Anger in Crime Fiction**: The `Crime Fiction` genre has a positive association with `anger` and a negative link with `joy`. 
                This suggests that crime narratives evoke intense emotions, reflecting the tense and dramatic nature of such plots.
    -   **Diverse Emotions in Drama:** The genre `Drama` exhibits a diverse emotional landscape, characterized by positive correlations with
                 `joy` and `sadness` and negative correlations with `fear`, `anger` and `surprise`. 
                This complexity in emotions implies the rich and varied nature of storytelling within dramas.
    """)


