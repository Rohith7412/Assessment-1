import nltk
from nltk.corpus import stopwords
import contractions as contract
import re
import streamlit as st
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text=text.lower()
    text=contract.fix(text) # Expanding the contractions
    text = re.sub(r'https?://\S+|www\.\S+|@\S+', '', text) # removing URLs, links
    text=re.sub(r'<.*?>','',text) # removing html tags
    text=re.sub(r'[^a-zA-Z\s]'," ",text) # removing punctuation and numbers
    text=re.sub(r'\s+','',text) # removing extra white space character
    return text

def remove_Stopwords(text):
    words=text.lower().split()
    filtered_words=[word for word in words if word not in stop_words]
    return words, filtered_words

st.set_page_config(
    page_title="NLP TEXT CLEANER",
    page_icon="",
    layout="wide"
)

st.title("NLP TEXT CLEANING AND STOPWORDS REMOVAL APP")
st.write("Enter raw text below to clean it and remove stopwords")

user_input=st.text_area(
    "Enter your text here:"
)

if st.button("process text"):
    cleaned_text=clean_text(user_input)
    original_words, filtered_words=remove_stopwords(clean_text)
    st.subheader("original Text")
    st.write(user_input)
    st.subheader("cleaned text")
    st.write(cleaned_text)
    st.subheader("Words before removing stopwords")
    st.write(original_words)
    st.subheader("words after removing stopwords")
    st.write(filtered_words)