<a href="https://colab.research.google.com/github/virajbhutada/ybi_foundation-task/blob/main/Movie_Recommendation_System_Colab.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
# **Movie Recommendation System**

# Movie Match: Revolutionizing Movie Recommendations with Close Match Algorithm

**Movie Match** is a groundbreaking recommendation system engineered specifically for movie enthusiasts. Powered by the Close Match algorithm, Movie Match meticulously analyzes user inputs, accommodating even the subtlest variations, to suggest movies that closely align with users' preferences.

**Close Match Precision**: Movie Match's Close Match algorithm ensures unparalleled accuracy, making it adept at handling typos, misspellings, or minor deviations in movie titles. Users can expect spot-on movie suggestions, enhancing their cinematic journey.

**Tailored Movie Suggestions**: Whether you're into classics, thrillers, or rom-coms, Movie Match tailors its recommendations based on your movie choices. Explore a world of cinematic brilliance with handpicked suggestions that match your unique taste.

**Seamless Movie Discovery**: Discovering movies has never been this intuitive. Movie Match simplifies the movie-search experience, offering a curated selection of films akin to your cinematic interests. Dive into a cinematic adventure that resonates with your preferences.

Join Movie Match today and embark on a cinematic adventure designed exclusively for your unique taste.


# **Objective**

The objective of this Movie Recommendation System is to provide users with highly accurate and personalized movie suggestions based on their preferences and inputs. Utilizing the Close Match algorithm, this system aims to offer spot-on recommendations, even accommodating minor deviations in movie titles. By tailoring suggestions to individual tastes and ensuring a seamless user experience, this system strives to enhance user engagement and satisfaction, making movie discovery an enjoyable and effortless process for every user.
**Data** **Source** - The dataset for this project was obtained from the YBI Foundation Kaggle repository. It includes information about movies, user ratings, and other relevant features necessary for building the recommendation system.
# **Import Libraries**
import pandas as pd
import numpy as np
# **Import Dataset**
df = pd.read_csv(r'D:\AI_project\movie-recommendation-system\Movie Recommendation System\Movies Recommendation (1).csv')
df.head()
df.info()
df.shape
df.columns
# **Get Feature Selection**


df_features = df[[ 'Movie_Genre', 'Movie_Keywords', 'Movie_Tagline', 'Movie_Cast', 'Movie_Director']].fillna('')
df_features.shape
df_features
x = df_features['Movie_Genre'] + '' + df_features['Movie_Keywords'] + '' + df_features['Movie_Tagline'] +''+ df_features['Movie_Cast']+ ''+ df_features['Movie_Director']
x
x.shape
# Get Feature Text Conversion to Tokens
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape
print(x)
# **Get Similarity Score using Cosine Similarity**

cosine_similarity computes the L2-normalized dot product of vectors. Euclidean (L2) normalization projects the vectors onto the unit sphere, and their dot product is then the cosine of the angle between the points denoted by the vectors.

 from sklearn.metrics.pairwise import cosine_similarity

Similarity_Score = cosine_similarity(x)

Similarity_Score
Similarity_Score.shape
**Get Movie Name as Input from User and Validate for Closest Spelling**
Favourite_Movie_Name = input(' Enter your favourite movie name :')

All_Movies_Title_List = df['Movie_Title'].tolist()
import difflib
Movie_Recommendation = difflib.get_close_matches (Favourite_Movie_Name, All_Movies_Title_List)
print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]
print (Close_Match)

Index_of_Close_Match_Movie = df [df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

# getting a list of similar movies

Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))
print (Recommendation_Score)



 len(Recommendation_Score)


# **Get All Movies Sorted Based on Recommendation Score for your Favourite Movie**

#sorting the movies based on their similarity score

Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse=True)
print (Sorted_Similar_Movies)

# print the name of similar movies based on the index

print('Top 30 Movies Suggested for You :\ n ')

i=1

for movie in Sorted_Similar_Movies:
   index = movie[0]
   title_from_index = df [df.index==index]['Movie_Title'].values[0]
   if (i<31):
    print(i, '.',title_from_index)
    i+=1
# **Top 10 Movies Recommended Based on Your Favorite Movie**

import difflib

Movie_Name = input('Enter your favorite movie name: ')

list_of_all_titles = df['Movie_Title'].tolist()

# Find close matches to the input movie name
close_matches = difflib.get_close_matches(Movie_Name, list_of_all_titles)

if close_matches:
    closest_match = close_matches[0]  # Get the closest match
    Index_of_Movie = df[df.Movie_Title == closest_match]['Movie_ID'].values[0]

    Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))

    sorted_similar_movies = sorted(Recommendation_Score, key=lambda x: x[1], reverse=True)

    print('Top 10 Movies suggested for you: \n')

    i = 1

    for movie in sorted_similar_movies:
        index = movie[0]
        if index < len(df):
            title_from_index = df[df.Movie_ID == index]['Movie_Title'].values[0]
            print(i, '.', title_from_index)
            i += 1
        else:
            print("Invalid index:", index)

        if i > 10:
            break
else:
    print('No close matches found for the entered movie name.')




Movie Match, the advanced Movie Recommendation System, is powered by the **Close Match algorithm**, ensuring precise and personalized movie suggestions. By employing fuzzy matching techniques, it adeptly handles minor input variations, such as typos or incomplete titles. This innovative approach guarantees spot-on recommendations, tailored exclusively for each user's cinematic taste.



In conclusion, Movie Match offers a seamless and immersive movie-watching experience. I'm delighted to assist you in discovering movies perfectly aligned with your preferences. Thank you for choosing Movie Match. For any inquiries or assistance, please don't hesitate to contact me. Happy movie watching!


Thank you for exploring our Movie Recommendation System! I hope you enjoy your personalized movie suggestions. If you have any questions or feedback, feel free to reach out. Happy movie watching!
