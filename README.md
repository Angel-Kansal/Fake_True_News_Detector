# 📰 Fake News Detector (AI/ML Project)

This project is an AI-powered Fake News Detection system that uses **Natural Language Processing (NLP)** and **Machine Learning** to classify news as either **Fake** or **Real**.

It was built using:
- Python
- Scikit-learn
- TF-IDF Vectorization
- Streamlit (for web app UI)

---

## 🚀 Live Demo

👉 [Click here to try it on Streamlit (if deployed)](https://your-streamlit-app-link)

---

## 📂 Project Structure
├── app.py # Streamlit frontend
├── data_prep.py # Data cleaning, model training
├── Fake.csv # Dataset: Fake news
├── True.csv # Dataset: True news
├── model.pkl # Trained ML model
├── vectorizer.pkl # Trained TF-IDF vectorizer
├── requirements.txt # Required Python libraries
└── README.md # Project description


---

## ⚙️ How It Works

1. `data_prep.py`:
   - Loads and cleans the Fake & True datasets
   - Combines, vectorizes, and trains a Logistic Regression model
   - Saves the model (`model.pkl`) and vectorizer (`vectorizer.pkl`)

2. `app.py`:
   - Creates a simple UI with Streamlit
   - Takes user input text
   - Loads model & vectorizer to classify the text as "FAKE" or "REAL"

---

## 🧠 ML Techniques Used

- **TF-IDF Vectorizer** for text feature extraction
- **Logistic Regression** for binary classification
- **Joblib** to save and load models

---

## ✅ Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## ⚙️ How It Works

1. `data_prep.py`:
   - Loads and cleans the Fake & True datasets
   - Combines, vectorizes, and trains a Logistic Regression model
   - Saves the model (`model.pkl`) and vectorizer (`vectorizer.pkl`)

2. `app.py`:
   - Creates a simple UI with Streamlit
   - Takes user input text
   - Loads model & vectorizer to classify the text as "FAKE" or "REAL"

---

## 🧠 ML Techniques Used

- **TF-IDF Vectorizer** for text feature extraction
- **Logistic Regression** for binary classification
- **Joblib** to save and load models

---

## ✅ Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## ⚙️ How It Works

1. `data_prep.py`:
   - Loads and cleans the Fake & True datasets
   - Combines, vectorizes, and trains a Logistic Regression model
   - Saves the model (`model.pkl`) and vectorizer (`vectorizer.pkl`)

2. `app.py`:
   - Creates a simple UI with Streamlit
   - Takes user input text
   - Loads model & vectorizer to classify the text as "FAKE" or "REAL"

---

## 🧠 ML Techniques Used

- **TF-IDF Vectorizer** for text feature extraction
- **Logistic Regression** for binary classification
- **Joblib** to save and load models

---

## ✅ Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```



---

## ⚙️ How It Works

1. `data_prep.py`:
   - Loads and cleans the Fake & True datasets
   - Combines, vectorizes, and trains a Logistic Regression model
   - Saves the model (`model.pkl`) and vectorizer (`vectorizer.pkl`)

2. `app.py`:
   - Creates a simple UI with Streamlit
   - Takes user input text
   - Loads model & vectorizer to classify the text as "FAKE" or "REAL"

---

## 🧠 ML Techniques Used

- **TF-IDF Vectorizer** for text feature extraction
- **Logistic Regression** for binary classification
- **Joblib** to save and load models

---

## ✅ Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```

*HOW TO RUN LOCALLY*
# Step 1: Train the model (optional)
python data_prep.py

# Step 2: Run the Streamlit app
streamlit run app.py

✨ Features
Fast, lightweight web interface (Streamlit)

Classifies news articles with high accuracy

Completely open-source and easy to customize

🙋‍♂️ Made With ❤️ By
Angel Kansal

19 y/o | B.Tech Student | Aspiring AI/ML Developer from Hapur, UP
GitHub: @Angel-Kansal



