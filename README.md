# 🎬 Movie Recommender System (Content-Based Filtering)

A smart **content-based movie recommendation system** built using **Python** and **Streamlit**.  
This project suggests similar movies based on their content — such as **genres, cast, director, and plot keywords** — using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Features

- 🎥 **Movie Recommendation:** Suggests movies similar to the one selected by the user.  
- 🧠 **Content-Based Filtering:** Uses movie metadata like genres, cast, and keywords.  
- ⚡ **TF-IDF & Cosine Similarity:** Determines how closely movies are related based on textual similarity.  
- 🧩 **Interactive UI:** Built with Streamlit for a clean and easy-to-use interface.  
- 🗂️ **TMDB 5000 Movies Dataset:** Reliable dataset with real-world movie information.  

---

## 🧰 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Language** | Python |
| **Framework** | Streamlit |
| **Libraries** | Pandas, NumPy, Scikit-learn, NLTK, Pickle |
| **Algorithm** | TF-IDF Vectorization + Cosine Similarity |
| **Dataset** | TMDB 5000 Movie Dataset (CSV) |

---

## 🧠 How It Works

1. The dataset is preprocessed to combine key textual features (overview, genres, keywords, cast, director).  
2. These features are converted into numerical form using **TF-IDF Vectorization**.  
3. **Cosine Similarity** measures the distance between movie vectors.  
4. When a user selects a movie, the system recommends top 5–10 similar movies based on similarity scores.

## 🖥️ System Architecture

User → Streamlit Frontend → Movie Data Processing (Python) → TF-IDF Vectorization → Cosine Similarity → Recommended Movies

Project Structure
├── app.py                # Streamlit frontend
├── movies.csv            # TMDB dataset
├── movie_list.pkl        # Preprocessed movie titles
├── similarity.pkl        # Similarity matrix (locally generated)
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignored files
└── README.md             # Project documentation

Learning Outcomes.

Applied content-based recommendation algorithms

Implemented TF-IDF vectorization and cosine similarity

Built a complete Streamlit web application

Learned how to handle large datasets and NLP features

Gained experience in deployable data science projects
