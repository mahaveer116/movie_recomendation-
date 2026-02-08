Movie Recommender System:

A content-based movie recommendation system built using Natural Language Processing (NLP) and cosine similarity.
The system analyzes movie metadata to recommend films that are similar to a user-selected movie, helping users discover relevant content.

Overview:

This project implements a content-based filtering approach where movies are recommended based on textual similarity between their descriptions, genres, and metadata.
It provides an intuitive and interactive web interface for browsing trending movies and exploring personalized recommendations.

Features:

Content-Based Filtering using movie metadata

TF-IDF vectorization with cosine similarity

Clean and modern user interface

Multiple recommendation types:

Similar Movies (TF-IDF based)

Genre-based recommendations

Trending movies section

Technology Stack:

Backend:
Python
FastAPI


Data preprocessing:
Machine Learning and NLP
scikit-learn
TfidfVectorizer
cosine_similarity
Natural Language Processing for text feature extraction

Frontend:
Streamlit

Screenshots:
1. Home Page – Trending Movies

The landing page displays trending movies along with a search interface that allows users to quickly find titles of interest.
![homepage](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/homepage.png)

2. Movie Details Page

Displays detailed information about a selected movie, including poster, release date, genres, and overview.
This page serves as the entry point for generating recommendations.
![Movie Details](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/Movie%20Details%20Page.png)
3. Similar Movies (TF-IDF) Recommendations
Content-based recommendations generated using TF-IDF vectorization and cosine similarity.
![Similar Movies](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/Similar%20Movies.png)
4. Genre-Based Recommendations

Additional recommendations based on genre matching to help users explore related content.
![Genre-Based](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/Genre-Based.png)

Dataset:

The system uses movie_recommendation.csv, which contains:

Movie titles

Genres

Release dates

Overview and descriptions

Additional metadata

How It Works:
Data Preprocessing:

Cleaning and normalizing movie metadata

Handling missing values:

Extracting text-based features

Feature Engineering:

TF-IDF vectorization of movie descriptions and genres

Creation of numerical feature vectors for each movie

Similarity Calculation

Cosine similarity computed between movie vectors

Movies ranked based on similarity scores

Recommendation Generation

Returns the top N similar movies for a selected title

Provides genre-based alternative recommendations

Usage:

Browse trending movies on the home page

Search for movies by title

View detailed information for a selected movie

Explore recommendations:

Similar Movies (TF-IDF)

Genre-Based suggestions

Key Algorithms:
TF-IDF Vectorization

Converts movie descriptions into numerical vectors based on term frequency and inverse document frequency.

Cosine Similarity

Measures similarity between two vectors:

similarity = (A · B) / (||A|| × ||B||)

Future Enhancements:

Collaborative filtering integration

User rating system

Personalized recommendations using watch history

Movie trailers and streaming links

Advanced filters (year, rating, language)

Hybrid recommendation approach

Contributing:

Contributions are welcome.
Please feel free to fork the repository and submit a pull request.

License:

This project is licensed under the MIT License.
See the LICENSE file for more details.

Author

Mahaveer
GitHub: https://github.com/mahaveer116
