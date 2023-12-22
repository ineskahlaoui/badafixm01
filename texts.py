import streamlit as st

def format_text(text):
    st.markdown("""<div class='justified-text'>""" + text +""" </div>""", unsafe_allow_html=True)

def introduction():
    st.markdown("""<div class='justified-text'>
    Dear movie adepts and graph gurus, welcome to a spectacle where movies and charts converge into a narrative as captivating as cinema itself…
    In our story, every frame is a figure and every genre a graph, as we delve into the rich dataset of 
    <a href="https://www.cs.cmu.edu/~ark/personas/" target="_blank">movies</a> and 
    <a href="https://saifmohammad.com/WebPages/AffectIntensity.htm" target="_blank">Emotion Intensity Lexicon</a> to see not just the 
    stories on screen but also the emotions they stir in us, all through the power of data!
    From the epic heroes of the Silent generation to the digital natives of Gen Z (us!),
    each bringing their own flair to the big screen, we propose you a century-long timeline a period rich with wars, 
    peace, crises, and prosperity in waves of drama, mystery, romance, and more. 
    No prior knowledge is required, just an appetite for discovery and a love for the silver screen.
    So, pop the popcorn, dim the lights, and let this data illuminate this new story of 
    cinema like you’ve never before. 🍿 Cameras rolling... Action! 🎬 
    </div>""", unsafe_allow_html=True)


def regression():
    st.subheader("Methodology")

    # Description of the methodology
    format_text("""
    An Ordinary Least Squares model was constructed for each genre using sentiment scores and the intensities of eight emotions as predictors. 
                The data underwent paired matching on countries, languages, generation, and runtime to mitigate the effect of confounding factors. 
                The heatmap displays the slopes of linear regressions between one-hot encoded genres and emotion intensities and sentiment score of movie plot summaries.
                 All visualized slopes are statistically significant \(p < 0.05\). 
                The slopes indicate the degree that an emotion or sentiment shapes the likelihood that a movie belongs to a genre. 
                Indeed, there are interesting patterns of emotional influence in some genres:
    """)

    st.subheader("Key Findings")

    format_text("""
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


def emotion_lines():
    format_text("""We observe that for all genres our average emotion score for years before 1940 tend to be more messy, 
                but this is an effect of the comparetively low number of movies release in these decades when compared to the following years. 
                Impressively, we can see that most genres do reach a stable ordering of emotions throught the years! 
                Words associated with fear are clearly dominant in Horror, Crime Fiction, and Thrillers, while Romantic comedies and 
                Romance movies are dominated by joy/trust followed by anticipation words. 
                It is really interesting to see that these genres seem to have their own emotional signature (at least on average!). 
                Let explore this a bit further... """)
    

def emotion_heatmap():
    format_text("""This heatmap gives us a better overal idea of how emotions are distributed in these genres. 
                Trust seems to be evoked in many genres except in Horror (I guess there's no trusting a guy chasing you with a chainsaw), 
                while fear is prevalent not only in obviously spooky/tense movie genres but also in action and science fiction! 
                This gives us a very interesting and general insight on how the edge/future of technology is portrayed in cinema. 
                Maybe we have a tendency to be pessimistic about the future?""")
    
def emotion_clusters():
    format_text("""As we observe it's not as simple as we thought, the latent emotion space of our movies 
                overlap quite a bit and don't really ressemble the clusters obtained by K-means. 
                Notheless, we can still notice that Romantic Comedy and Romance separate pretty well from 
                Action/Adventure, Thriller, Horror. If we want to actually discriminate movie genres based 
                on emotions we'd need a more sophisticated approach. 
                We'll come back to this later...""")
    

def emotion_generations():
    st.markdown("""As we can see it doesn't seem to change at all! 
                The average emotional content of the summaries is basically the same to all generations.""")
    

def pie_introduction():
    format_text("""The CMU Movie Summary Corpus Dataset consists of 42,207 movie plot summaries 
                and their corresponding metadata.  As the number of genres in this dataset are diverse, 
                with 364 genres in total, we decided to focus on the top 10 genres in the whole dataset, and analyses 
                how these genres vary across generations.""")
    
def pie_analysis():
    format_text("""Thrillers and dramas take the cake (or the pie actually 😉), 
                each comprising just over 21% of all movies. This suggests a collective leaning towards intense, 
                emotionally charged narratives gripping the audience. Or is that actually true, and can we quantify this intensity of narratives?  
                We are coming back to this question a little bit later in our story.""") 
    format_text("""Short films and crime fiction, each at 11.9%, remind us that brevity can be the soul of wit and intrigue: 
                they capture the essence of succinct storytelling in the form of short narrative. 
                But was this always the case? So, how do these preferences play out across different generations?""")