import streamlit as st


def format_text(text, size="18px", bottom_margin="16px"):
    st.markdown(f"""<div class='justified-text' style='text-align: justify; font-size: {size}; margin-bottom: {bottom_margin};'>{text}</div>""", unsafe_allow_html=True)


def introduction():
    format_text("""Dear movie adepts and graph gurus, welcome to a spectacle where movies and charts converge into a narrative as captivating as cinema itself…
    In our story, every frame is a figure and every genre a graph, as we delve into the rich dataset of 
    <a href="https://www.cs.cmu.edu/~ark/personas/" target="_blank">movies</a> and 
    <a href="https://saifmohammad.com/WebPages/AffectIntensity.htm" target="_blank">Emotion Intensity Lexicon</a> to see not just the 
    stories on screen but also the emotions they stir in us, all through the power of data!
    From the epic heroes of the Silent generation to the digital natives of Gen Z (us!),
    each bringing their own flair to the big screen, we propose you a century-long timeline a period rich with wars, 
    peace, crises, and prosperity in waves of drama, mystery, romance, and more. 
    No prior knowledge is required, just an appetite for discovery and a love for the silver screen.
    So, pop the popcorn, dim the lights, and let this data illuminate this new story of 
    cinema like you’ve never before.""") 
    format_text("""🍿 Cameras rolling... Action! 🎬 """)


def regression_intro():
    format_text("""To what degree can emotional intensities and the positive/negative sentiment 
                help shape the genre? We seek the answer in regression analysis. """, bottom_margin = "60px")

def regression():
    format_text("""We constructed an ensemble of Ordinary Least Squares models, one for each genre, 
                with paired matching on country, language, generation, and runtime of the movies. 
                The resulting heatmap of statistically significant (p<0.05) linear regression slopes 
                portrays how the different genres are woven by hues of emotions and sentiments. 
                Positive values indicate a positive association of the emotion or the sentiment 
                score with the likelihood that a movie belongs to this genre, and vice versa. 
                Now, let’s begin our quest to the land of genres and visit the emotional building blocks 
                that shape each one.
    """)

def regression_findings():
    format_text("""The Thriller genre stands as the most compelling connection with emotions. 
                Fear and joy correlate positively and negatively with this genre, respectively, 
                aligning with its weakly negative relationship with the sentiment score. 
                You can’t stay chill when unraveling the mysteries of a Hitchcockian plot, can you? 
                Contrasting with Thriller, Romantic Comedy dances with joy but flinches at fear. 
                These trends paint a light-hearted atmosphere within the genre. In Crime Fiction, 
                anger takes center stage while joy seems out of place, mirroring the tense and dramatic 
                nature in crime narratives. As a container of diverse emotions, the Drama genre exhibits 
                positive correlations to joy and sadness and negative correlations to fear, anger, and surprise, 
                implying the rich and varied nature of storytelling within dramas. """)

def emotion_lines_intro():
    format_text("""Time to unravel the emotional content of movie genres over the ages! 
                Are the eight basic emotions sprinkled randomly across genres, or do they follow predictable trends? 
                Let's find out!""", bottom_margin = "60px")
    

def emotion_dataset():
    format_text("""
                We've delved into the treasure trove known as the 
                <a href="http://saifmohammad.com/WebPages/AffectIntensity.htm" target="_blank">NRC Emotion Intensity Lexicon</a>
                 by the 
                <a href="https://arxiv.org/abs/1704.08798" target="_blank">Dr. Saif M. Mohammad and team</a> to experience an emotional odyssey through the realm of movies. 
                It's like a dictionary, but for emotions! Each word in this manually built dictionary has a score on a scale of 0 to 1, 
                using the 
                <a href="http://saifmohammad.com/WebPages/BestWorst.html" target="_blank">Best-Worst Scaling method</a>, 
                for each one of eight basic emotions: 
                fear, joy, anger, trust, anticipation, disgust, sadness, and surprise. 
                Armed with this lexicon, we've scored the emotional content of every word in our plot summaries, 
                giving us an emotional fingerprint of all of our movies! Let's hop on the feels train and see 
                what sort of cool stuff we can get from emotions in movies!""")


def emotion_lines():
    format_text("""Let's now hop on our cinematic time machine! 
                Before 1940, the overall emotions seem to get a bit wild – well, not because people were more wild, 
                just because of the sparse movie releases. But as we fast forward, 
                some genres seem to find their emotional fingerprints. 
                Horror, Crime Fiction, and Thrillers? Fear takes the lead. 
                Romantic comedies and Romance? It's all about joy, trust, and a hint of anticipation. 
                Each genre owns its unique emotional signature – cinema's secret language! 
                Let's keep on riding this emotional roller coaster! """, bottom_margin="60px")
    

def emotion_heatmap():
    format_text("""Let's now look at the emotion heatmap – our aggregate of cinematic vibes! 
                Trust is the star of the show, making appearances in various genres 
                (except Horror, where trusting a chainsaw-wielding person chasing you might not end well). 
                Fear, on the other hand, isn't just confined to spooky flicks – it's chilling with 
                the action and science fiction squads too! This paints an intriguing picture of 
                how cinema sees the cutting edge and future tech. Are we a tad pessimistic about what lies ahead?""")

def emotion_clusters_intro():
    format_text("""With all the clues pointing to genres having their own emotional fingerprints, 
                we couldn't resist asking: Can we spot a movie genre just by feeling the vibes in its summary? 
                Time to put our detective hats on and dive into the world of emotion clustering – 
                let the genre-guessing games begin!""")

def emotion_clusters():
    format_text("""Well... turns out our movie emotions are a bit of a mystery! 
                The emotional universe of our films doesn't neatly align with the clusters we envisioned. 
                Nevertheless, amidst the overlapping emotions, a glimmer of distinction emerges. 
                Romantic Comedy and Romance movies seem to cluster away from the pack of Action/Adventure, 
                Thriller, and Horror. But if we're serious about playing matchmaker with genres and emotions, 
                it seems a more sophisticated strategy is in order. Stay tuned, because we're just warming 
                up – there's more cinematic magic to unravel later on!""")
    

def emotion_generations_intro():
    format_text("""Time for an emotion check through time! 
                Do the emotions of cinema evolve with each generation, 
                or is the emotional script a timeless tale? 
                Let's check how different emotions unfold across the ages!""", bottom_margin="60px")
def emotion_generations():
    format_text("""It appears the cinematic emotions are doing the time warp! Across generations, 
                the average emotional content in movie summaries seem to be caught in a time loop, ever unchanging!""")
    
def movies_released_per_generation():
    format_text("""The CMU Movie Summary Corpus Dataset consists of 42,207 movie plot summaries 
                and their corresponding metadata. For the purpose of the analysis, and considering the large number
                of movies it contains, we suppose this dataset depicts an accurate representation of the proportion
                of movie released per generation. """)
    format_text("""Let's take a quick trip throughout time, looking at how many movies have been produced by generation. """, bottom_margin = "60px")
    


def movies_released_analysis():
    format_text("""First up, the Lost Generation, born around the time when movies were just starting, 
                which explains the lack of numerous movies at that time. 
                Throughout the generations, the number of movies continued to grow. Notably, 
                the Baby Boomers really saw things take off, with 4,750 movies released at that time. 
                This was when color TV and rock&roll were big, so movies had to keep up with the exciting times!""")

    format_text("""The Millennials take things up a notch with a big jump to 7,636 movies. 
                Thanks to the internet, making and especially watching movies got a lot easier. 
                This explains the rapid growth between this generation and the previous one. Generation Z has seen 
                the most so far, with a whopping 14,298 movies. 
                With smartphones, tablets, and streaming (illegal or not 😉), watching movies at any time, 
                any place, with or without internet connection, became the norm.""")

    format_text("""With Generation Alpha, we see fewer movies being made, 3,272. 
                This is simply explained by the fact that the dataset ranges until 2014, just 4 years after the 
                start of this generation, thus not being an accurate representation of the trends in the cinema 
                world for this generation. However, in the 4-year span where data is available, we can see that 
                this generation achieved a number of movies almost as large as the Silent generation. 
                Technology has made a lot of progress since then, and movie making became more and more popular, 
                and easier! """, bottom_margin="30px")



def pie_introduction():
    format_text(""" As the number of genres in CMU Movie Summary Corpus dataset is large, 
                with 364 genres in total, we decided to focus on the top 10 genres in the whole dataset, and analyses 
                how these genres vary across generations.""")
    
def pie_analysis():
    format_text("""Thrillers and dramas take the cake (or the pie actually 😉), 
                each comprising just over 21% of all movies. This suggests a collective leaning towards intense, 
                emotionally charged narratives gripping the audience. Or is that actually true, and can we quantify this intensity of narratives?  
                We are coming back to this question a little bit later in our story.""") 
    format_text("""Short films and crime fiction, each at 11.9%, remind us that brevity can be the soul of wit and intrigue: 
                they capture the essence of succinct storytelling in the form of short narrative. 
                But was this always the case? So, how do these preferences play out across different generations?""", bottom_margin = "60px")
    

def heatmap_analysis():
    format_text("""We implemented a heatmap to transition from the broad view of genre popularity 
                to a focused lens on generational predilections. For the Lost and Greatest generations, 
                the data is sparse, indicating fewer cinematic offerings or perhaps a limitation in data
                 collection for those eras. This indicates that movies that are popular across all generations
                 may not be popular for a specific generation.""")
    format_text("""However, the Baby Boomers seem to have expanded the cinematic canvas, showing a more diverse
                 set of preferences, with no single genre overwhelmingly dominating. This diversity grows further 
                with Gen X, where we see a significant uptick in thriller and drama, indicating a turn towards 
                intense, thought-provoking cinema. The Millennials and Gen Z take this evolution a step further: 
                the heatmap shows bright pink and purple with thrillers and drama movies, highlighting a generation 
                seemingly interested in suspense, action and emotional arcs 💃🕺.""")
    format_text("""With this generational perspective in mind, we now turn to a stacked bar chart to understand 
                how these genre preferences stack up proportionally over time, and to see whether a cultural shift in 
                the ‘moods’ and attitudes of society characterised by genres in noticeable. """, bottom_margin = "60px")


def stacked_genres_analysis():
    format_text("""The chart above enhances our previous insights, layering genre upon genre to form a proportional
                 look at cinematic tastes over time. We observe that the Lost generation's bar is dominated by a 
                single genre, Short Films, whereas the ensuing generations display a more 'mixed' mix, 
                indicating a broadening of interests and perhaps, an increase in the variety of films being produced. 
                This is not surprising, since at that time period the Lost generation’s focus was short films: 
                longer films, that were then categorised into genres themselves, were only introduced at the end of that
                 generation.""")
    format_text("""As we move from left to right, from oldest to newest generation, there’s a visible diversification 
                in genres consumed. The Silent Generation's bar shows an increase in dramas and thrillers, 
                a pattern that's consistently amplified in almost all following generations.""")
    
def parallel_genres_intro():
    format_text("""However, this representation might not be the most accurate, as it does not take into account the 
                top genres for each generation. Let's that a closer look at this!""", bottom_margin = "30px")
    
def parallel_genres_analysis():
    format_text("""This parallel graph allows us to observe the shifts in cultural cinematic preferences 
                through genres. Witness the robust presence of drama, present across almost all generations, 
                suggesting a universal resonance with the poignant effect of this genre to the watcher. 
                Drama might constitute an escape from reality to the watcher like no other genre.""")
    
    format_text("""Generation-specific genres emerge and retreat. 
                As we can see, 21 genres are popular over the years, contradicting the initial top 10 genres
                 we found across all generations. This informs us of a change in preferences over generations, 
                but also the emergence of new genres. As an example, before Gen Z, ‘LGBT’ genre did not exist. 
                The fact that this genre not only exists but became popular amongst that generation shows 
                the true meaning of inclusivity in the cinematic world. ‘Family films’ also appear in the last 
                2 generations, Millennials and Gen Z, which reinforces the idea that newer generations value 
                family experiences a lot more than previous ones, more focused on work and making a living during dark times. 
                This also depicts the world as is: times of war call for work and action - and less family time - and latter times, 
                thus calmer times in a worldwide setting,
                allow people to focus on other aspects of their lives, such as family.""")
    format_text("""To the opposite spectrum, some genres disappeared. 
                The top right of the graph shows that silent film were popular once, with  the Lost, 
                Greatest and Silent generations, but quickly faded after the expansion of technology and the development 
                of movie equipments.""")
    format_text("""We wonder though if these feelings and emotions we are talking about are translated and visible in certain genres...""")
    

def generations_explained():
    format_text("""
    From the 20th to the 21st centuries, distinct generations have emerged, 
                each shaped by unique historical and cultural events. 
                The story of these generations is a voyage through war and peace, prosperity and hardship, 
                revolution and the rise of the digital age 💻.""")

    format_text(""" <strong>The Lost Generation (born between 1883 and 1900)</strong> emerged right before World War I and the 
                roaring twenties, and lived through these historical periods. 
                They were marked by a profound sense of disillusionment from the war's devastation, 
                and this was reflected in the era's shift toward modernist art and literature.""")

    format_text(""" <strong> The Greatest Generation (1901–1927)</strong> was forged under the harsh conditions of the Great Depression,
                 instilling in them the values of frugality and a strong work ethic. 
                Their resilience was further tested during World War II, which cultivated a deep sense of duty, 
                sacrifice, commitment to community and a respect for authority.""")

    format_text("""<strong> The Silent Generation (1928–1945)</strong> grew up amongst economic hardship and conflict but matured into the 
                stability of the post-war boom. This era shaped them into conformists with a strong civic sense, 
                valuing stability and discretion about personal struggles.""")

    format_text("""<strong> The Baby Boomers (1946–1964)</strong> burst onto the scene during the transformative years of the civil 
                rights movement, the Vietnam War, and the sexual revolution. 
                They were characterised by their willingness to challenge social norms and authority, 
                unlike previous generations, valuing individualism, equal rights and personal freedom.""")

    format_text(""" <strong> Generation X (1965–1980)</strong> came of age in a period tinged with economic uncertainty and changing 
                family dynamics. Independence, resilience, and a desire for a healthy work-life balance define
                 this generation, which is often viewed as skeptical yet value-driven.""")
                
    format_text(""" <strong> The Millennials (1981–1996)</strong> entered adulthood with the internet revolution at their fingertips, 
                shaping their values around connectivity, innovation, and a global perspective. 
                They are known for prioritising diversity, equality, sustainability, and valuing experiences over material
                 possessions. This generation connects with Generation X in a certain sense.""")
                
    format_text("""<strong> Generation Z (1997–2009)</strong> represents the true digital natives (us!), for whom inclusivity, 
                individuality, and authenticity are core values. Raised during a global recession, 
                they are seen as pragmatic and financially astute, with strong commitments to social justice 
                and environmental issues.""")

    format_text("""<strong> Generation Alpha (2010–2024)</strong>, the youngest and emerging generation, is still being shaped 
    \(our brothers and sisters - if any!). They are the real children of the digital age, surrounded by advanced technology and AI.
                 Early indications suggest they will prioritise digital literacy, mental health, 
                and the pressing environmental concerns of their time.""")

    format_text("""Each of these generations has left and will leave an indelible mark on the world, 
                not just through the values they uphold and the culture they create but also through the art 
                they consume and produce, including the movies that define their times.
    """)

def sentiment_score_distribution():
    format_text("""We wanted to take a deeper journey into the evolution of movies throughout time using the TextBlob tool. 
                We compute the sentiment score of each plot summary corresponding to every movie to reflect the story's heart and averaged it, 
                pulsating between the extremes of -1 and 1, where every nuance of emotion from the darkest despair to the brightest joy is captured. 
This histogram reveals that most movie plot summaries tend to be a bit on the positive side, with a peak around a sentiment score of 0.15. 
                This means that when all the stories are averaged out, they're generally more uplifting than downbeat. 
                It’s rare to find a movie plot summary that's extremely negative, as the left side of the chart, which represents the sadder scores, is quite empty.""")


def sentiment_intro():
    format_text("""We decided to take a closer look at 4 of the main genres in the dataset, 
    and analyse the overall sentiment score of the movie plot summaries for each genre. """, bottom_margin = "40px")

def sentiment_analysis():
    format_text("""The Lost Generation's sentiment score is like a mysterious zero, 
                not because they didn't feel anything, but because their movie plot summaries got lost in time! 
                Thrillers roller-coastered through generations, from being a hit escape room for the Silent 
                generation, to not quite thrilling for the Greatest generation. """)
    format_text("""On the other hand, Baby Boomers and Gen X jumped back on the thrill ride, 
                while Millennials and Gen Z swiped left for deeper plots and internet vibes 🕺. 
                Romantic comedies and horrors zigzagged similarly, with each generation scripting their own 
                love and scare. And short films? They hit a sentimental peak with Gen X, showing sometimes 
                less is more, except for Gen Alpha, who are probably too busy with virtual reality to bother 
                with short old-school flicks!""")
    

def movie_releases_intro():
    format_text("""Nothing puts as more in our feels than life itself! 
                Ever felt like the exact type of movie you wanted to watch was in the cinema? 
                This may be a coincidence, or not... Do movies reflect what society has gone through recently? 
                To investigate the relationship between the emotions portrayed in movies in different time periods, 
                we will first look into how the movie industry has changed over generations, and how time has impacted 
                this. More specifically, throughout this section we will delve into historical events that 
                profoundly resonated across the globe.""")
    format_text("""Starting with <strong>World War II (1939-1945)</strong>, 
                we will explore the emotional imprint left by this a monumental confrontation world-wide, 
                and its effect on movie production.""")
    format_text("""Similarly, the <strong>Cold War era (1947-1960)</strong> was characterized by a high-stress rivalry 
                among the world’s leading nations. This cast a long shadow over the latter half 
                of the 20th century, and we expect movies at this time to have served as a lens 
                through which audiences could process the complex global tension.""")
    format_text("""Lastly, the tragic events of <strong>September 11th, 2001</strong>, 
                represent another pivotal moment with a profound emotional and cultural impact. 
                The aftermath of these attacks saw a surge in films that delved into themes of national security, 
                international politics, and the complexities of global threats to peace and safety. """, bottom_margin="30px")
    format_text("""First up, how has the number of movies released evolved with time? 
                It’s like making popcorn – slow at first, then bursting forth in an explosion of cinematic abundance! 
                 Below, we see how cinema has mirrored society as generations progress.""")
    

def movie_releases_analysis():
    format_text("""The above graph reflects the journey from black-and-white 
                classics to 3D spectacles since it is clear that technological advancements 
                have really paved the way for an exponential growth in cinema production. 
                If examining the historical periods mentioned above, during WW2 there is a clear 
                decrease in movie production. Moreover, in the Cold War era, despite having an overall 
                increase in production, there were lots of ups and downs. On the other hand, after 9/11 
                there is not an observable decrease, and we infer that filmmakers channelled the complexities
                 arisen into new stories.""")
    format_text("""Naturally, the progression of movie production over time has varied 
                significantly from one country to another, some being hubs of innovation and cultural 
                melting pots, which turned them into movie-producing powerhouses. 
                We delve into these geographical shifts by plotting the distribution of number 
                of movies released per country in this interactive world map.""")
    
def world_map_analysis():
    format_text("""The graph above illustrates how certain regions have been more prolific 
                in their cinematic output, with the strongest concentration of movie production appearing in North America. 
                This is indicated by the deep blue shading, which suggests a movie count significantly higher than 20,000,
                 reflecting the region's status as a dominant force in the film industry.""")
    format_text("""Europe and Asia also show substantial contributions to global cinema, 
                as evidenced by the varied shades of purple and pink, indicating a from moderate to 
                high movie contributions. However, these figures don't come close to the towering movie
                 output represented by the deep blue that marks the film industry of the region akin to the USA.""")
    format_text("""In contrast, Africa, South America, and others display lighter shades, 
            implying a lower volume of movie production.""") 
    format_text("""The global map gives us a snapshot of movie production distribution, 
                highlighting regional leaders. To understand the dynamics behind these numbers, 
                let's delve into the line graph below, which traces the historical rise and fall of 
                movie production providing context to the flow of cinema across the top producing countries.""")
    

def world_lines_analysis():
    format_text("""The United States demonstrates a dramatic surge in movie 
                production starting around the early 20th century, with a particularly 
                pronounced increase from 1925-1935 and from the 1980s up to the early 2000s. India shows 
                a steady increase in film production from the mid-20th century, with growth becoming more 
                pronounced from the 1970s onwards. This aligns with the expansion of Bollywood and its global influence.
                 The line for Japan shows modest, stable growth throughout the 20th century, with no sharp peaks or drops.
                 This suggests a consistent film production rate without the dramatic fluctuations seen in other regions.
                 France and the United Kingdom have relatively lower and stable production numbers compared to the USA 
                and India, with slight increases and decreases throughout the century but without any drastic changes.""")
    format_text("""Regardless of the peak steepness, there is a clear increase 
                in production for the five countries between the late 20th century 
                and the beginning of the 21st century. This uptick marks a vibrant era in film, 
                driven by technology breakthroughs, and a growing appetite for varied narratives, 
                taking the movie business to exciting new levels. Conversely, after 2006 there is a decrease
                 trend for all countries, which suggests a possible shift in the industry, perhaps due to the
                 rise of digital streaming platforms or changing consumer viewing habits.""")
    format_text("""Regarding the marked historical period on the graph, during World War II, 
                there's a noticeable dip in movie production for most countries, which is a likely 
                reflection of the global focus on the war effort. The Cold War period doesn't show a 
                significant decline in movie production for the countries represented, suggesting that 
                the film industry continued despite the geopolitical tensions. As mentioned previously, 
                9/11 did not result in a decrease in movie production.""", bottom_margin="40px")
    
    format_text("""So… coming back to the main question! How does time and history affect the movie industry in terms of emotions? For this analysis, we used a Natural Language Processing (GoEmotions) algorithm, which when inputted a text, it returns one or several emotions out of a 28 emotions dictionary. In this section we seek to investigate whether historical events are reflected in emotions portrayed in movies were affected by history. """)
    format_text("""The input to the model were the movie plot summaries, which resulted in a range of predicted emotions for each movie, and these could be grouped to represent emotions over time. As stablished, the periods that will be investigated are WW2, Cold war and 9/11, with an additional control period. The years chosen for the analysis are 1947-1952 (post-WW2 era), 1980-1985 (Cold War era), 2003-2008 (post-9/11 era) and 1996-2001 (control). For all a fixed period of 5 years was used. The start of this period was fixed to two years after the historical event for WW2 and 9/11, to allow a buffer for the film industry to respond to and reflect these events in cinema. For the Cold War, a mid-period range was selected to capture the ongoing sentiments during this prolonged era, while the control period of 1996-2001 offers a baseline against which to measure changes in emotional trends in cinema outside of these major historical contexts.""")
    format_text("""To visually represent the range of emotions in these time periods we employed the technique of creating word clouds with the words extracted by GoEmotions from the movie plots. The size of words within these clouds correspond to their frequency of occurrence. These can be seen below.""")



def world_cloud_analysis():
    format_text("""Looking at all the above, the first observation is that there is not a major difference between historical and the control period. Realization is dominant and common across all word clouds, which we believe is an emotion that can be easily found in every movie. Thus, despite its abundant frequency, we will focus on the rest. In the historical events, there is a clear pattern of emotions such as disappointment, fear, anger, sadness, annoyance, being frequent. Nevertheless, other emotions such as joy are also consistently present. Moreover, the control period did not exhibit a significant divergence from this pattern. This suggests an enduring diversity of emotional experiences depicted in cinema!""")
    format_text("""It is important to note the model used was pre-trained on user tweets, which often have emotional expressions compared to movie plot summaries. This disparity in the training data could potentially explain any limitations in our findings. The model may not have performed as effectively when applied to movie-related text, leading to potential inaccuracies in the analysis.""")