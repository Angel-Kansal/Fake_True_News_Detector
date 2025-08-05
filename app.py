import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# UI
st.title("📰 Fake News Detector")
st.write("Enter a news article or headline to check if it is real or fake:")

user_input = st.text_area("News Content")

if st.button("Predict"):
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]
    label = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
    st.success(f"Prediction: {label}")
