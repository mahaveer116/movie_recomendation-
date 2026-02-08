Movie Recommender System
A content-based movie recommendation system built using Natural Language Processing (NLP) and cosine similarity. The system analyzes movie features to suggest similar films based on user selection.
Features

Content-Based Filtering: Uses movie metadata to find similar movies
Cosine Similarity: Measures similarity between movies using TF-IDF vectors
Interactive UI: Clean, modern interface for browsing and discovering movies
Multiple Recommendation Types:

Similar Movies (TF-IDF based)
Genre-based recommendations
Trending movies section



Technology Stack

Backend: Python, Flask
Machine Learning: scikit-learn (TfidfVectorizer, cosine_similarity)
NLP: Natural Language Processing for text feature extraction
Data Processing: pandas, numpy
Frontend: HTML, CSS, JavaScript

Screenshots
1. Home Page - Trending Movies
The landing page displays a collection of trending movies with an intuitive search interface. Users can browse through popular titles and use the keyword search to find specific movies.
   ![homepage](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/homepage.png)

2. Movie Details Page
Detailed view of a selected movie showing the poster, release date, genres, and plot overview. This page serves as the gateway to personalized recommendations.
 ![Movie Details Page](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/Movie%20Details%20Page.png)
3. Similar Movies (TF-IDF) Recommendations
Content-based recommendations using TF-IDF vectorization and cosine similarity. The system analyzes movie descriptions and metadata to find the most similar films.
![Similar Movies](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/Similar%20Movies.png)
4. Genre-Based Recommendations
Additional recommendations based on genre matching, providing users with more options that share similar thematic elements with their selected movie.
![Genre-Based](https://github.com/mahaveer116/movie_recomendation-/blob/793286193096f5bee9a3aca94681d7ee8a694ef3/Genre-Based.png)
Dataset
The system uses movie_recommendation.csv which contains:

Movie titles
Genres
Release dates
Overview/descriptions
Other metadata

How It Works

Data Preprocessing:

Cleaning and normalizing movie metadata
Handling missing values
Feature extraction from text fields


Feature Engineering:

TF-IDF vectorization of movie descriptions and genres
Creating feature vectors for each movie


Similarity Calculation:

Cosine similarity between movie vectors
Ranking movies based on similarity scores


Recommendation Generation:

Returns top N similar movies for a given title
Provides genre-based alternatives



Usage

Browse Movies: View trending movies on the home page
Search: Use the search bar to find specific movies by title
View Details: Click on any movie to see its full details
Get Recommendations:

View "Similar Movies (TF-IDF)" for content-based recommendations
Check "More Like This (Genre)" for genre-based suggestions



Key Algorithms
TF-IDF Vectorization
Converts movie descriptions into numerical vectors based on term frequency and inverse document frequency.
Cosine Similarity
Measures the cosine of the angle between two vectors to determine similarity:
similarity = cos(θ) = (A · B) / (||A|| × ||B||)
Future Enhancements

Collaborative filtering integration
User rating system
Personalized recommendations based on watch history
Movie trailers and streaming links
Advanced filters (year, rating, language)
Hybrid recommendation approach

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
