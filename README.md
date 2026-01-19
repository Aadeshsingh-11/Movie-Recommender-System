# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **Python, Machine Learning, and Streamlit**.  
This app recommends movies similar to the one selected by the user based on textual features like genres, keywords, cast, and crew.

🔗 **Live Demo:**  
https://movie-recommender-system-ne3r26mivrnteu3cpvvph7.streamlit.app

---

## 🚀 Features

- 📌 Recommends top 5 similar movies
- 🎭 Content-based filtering (no user ratings required)
- ⚡ Fast and interactive Streamlit UI
- ☁️ Deployed on Streamlit Cloud
- 🧠 Uses NLP techniques and cosine similarity

---

## 🛠️ Tech Stack

- **Python**
- **Pandas & NumPy**
- **Scikit-learn**
- **Natural Language Processing (NLP)**
- **Streamlit**
- **Git & GitHub**

---

## 📂 Project Structure

Movie-Recommender-System/
│
├── app.py # Streamlit UI
├── main.py # Recommendation logic
├── main.ipynb # Data preprocessing & model training
├── movie_dict.pkl # Processed movie data
├── movies.pkl # Movie dataframe
├── tmdb_5000_movie.csv # Dataset
├── tmdb_5000_credit.csv # Dataset
├── requirements.txt
└── README.md

---

## 🧠 How It Works

1. Movie metadata is preprocessed using NLP techniques.
2. Important features are combined into a single **tags** column.
3. Tags are vectorized using **CountVectorizer**.
4. **Cosine similarity** is calculated at runtime to find similar movies.
5. Top 5 most similar movies are displayed to the user.

---


# 📜 License

This project is for educational purposes.

