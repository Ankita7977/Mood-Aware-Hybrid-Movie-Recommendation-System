# 🎬 Mood-Aware Hybrid Movie Recommendation System

A hybrid movie recommendation system that suggests movies based on:
🎥 A movie you like
😊 Your current mood
It combines content-based filtering with mood-based genre filtering and fetches real-time movie details using the TMDB API.

---

## 🚀 Live Demo
[Click Here to View Live App](https://mood-aware-hybrid-movie-recommendation-system-7cgsj8nqkbp8qaec.streamlit.app/)

---

## 📌 Problem Statement
This project improves recommendation quality by integrating mood-based filtering with content-based similarity to deliver more personalized and context-aware recommendations.

---

## 📌 Project Overview
This project combines:

### 1. Content-Based Filtering
- CountVectorizer  
- Cosine Similarity
  
### 2. Mood-Based Filtering
- Each mood mapped to specific genres  
- Recommendations filtered based on mood

### 3. TMDB API Integration
- Fetches movie posters  
- Ratings  
- Release year  
- Overview  

---

## 📊 Algorithms & Techniques Used

- **CountVectorizer** for text vectorization
- **Cosine Similarity** for content-based filtering
- Genre-to-Mood mapping logic
- API integration using Requests

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- TMDB API  
- Requests  

---

## 📂 Project Structure
```
Mood-Aware-Hybrid-Movie-Recommendation-System/
│
├── app.py
├── movies_dict.pkl
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```
---

##⚙️ Installation & Setup
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ankita7977/Mood-Aware-Hybrid-Movie-Recommendation-System.git
```
### 2️⃣ Navigate to the project folder
```bash
cd Mood-Aware-Hybrid-Movie-Recommendation-System
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the app
```bash
streamlit run app.py

---

## 🔐 Environment Variables
This project requires a TMDB API key.
⚠️ Do not share your API key publicly.

Create a `.streamlit/secrets.toml` file and add:

```toml
TMDB_API_KEY = "your_api_key_here"

---

## ⚙️ How It Works
1. User selects a movie.  
2. System finds similar movies using cosine similarity.  
3. Filters results based on selected mood.  
4. Fetches movie details using TMDB API.  
5. Displays top recommendations with posters and ratings.

---

## ✨ Features
- 🎥 Movie-based recommendations  
- 😊 Mood-based filtering (Happy, Sad, Excited, etc.)  
- ⭐ Displays movie ratings
- 📅 Shows release year
- 🖼 Displays movie posters 
- 📖 Shows movie overview
- ⚡ Fast and interactive user interface built with Streamlit

---

## 🎯 Key Highlights
- Hybrid recommendation approach  
- Mood-aware personalization  
- Real-time API integration  
- Clean and responsive UI  

---

## 🚀Future Improvements
- Add user authentication system
- Implement collaborative filtering
- Add user rating-based learning
- Improve UI/UX design
- Docker deployment
- Mobile responsive layout

---

## Author
Ankita Prajapati  
Aspiring Data Scientist | Machine Learning Enthusiast
