import streamlit as st
import joblib

model=joblib.load("C:/Users/user/OneDrive/Desktop/nlp/NLP/host/sentiment-model.pkl")

sentiment_labels={'1':'Positive','0':'Negative'}

st.title("Sentiment Analysis")

user_input=st.text_area("Enter your text here:")

if st.button("Predict"):
    predicted_sentiment = model.predict([user_input])[0]
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]

    st.info(f"predicted sentiment: {predicted_sentiment_label}")