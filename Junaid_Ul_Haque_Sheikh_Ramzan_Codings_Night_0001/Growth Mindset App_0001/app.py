import streamlit as st
import pandas as pd
import nltk
from textblob import TextBlob

# Download NLTK resources
nltk.download('punkt')

def text_analysis(text):
    word_count = len(text.split())
    char_count = len(text)
    sentiment = TextBlob(text).sentiment.polarity
    return word_count, char_count, sentiment

# Streamlit UI
st.title("Growth Mindset Challenge: Text Analyzer")
st.write("Enter text below to analyze word count, character count, and sentiment.")

user_text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_text:
        words, chars, sentiment = text_analysis(user_text)
        st.write(f"Word Count: {words}")
        st.write(f"Character Count: {chars}")
        st.write(f"Sentiment Score: {sentiment}")
        
        if sentiment > 0:
            st.success("Positive Sentiment 😊")
        elif sentiment < 0:
            st.error("Negative Sentiment 😞")
        else:
            st.warning("Neutral Sentiment 😐")
    else:
        st.warning("Please enter some text to analyze.")
