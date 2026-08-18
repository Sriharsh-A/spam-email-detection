import re
import streamlit as st
import joblib

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="",
    layout="centered"
)

model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


st.title("Spam Email Detector")

st.write("Paste an email below and check whether it is spam or not spam.")

email_text = st.text_area(
    "Email Message",
    height=250,
    placeholder="Paste your email here..."
)

if st.button("Check Email", use_container_width=True):

    if not email_text.strip():
        st.warning("Please enter an email message.")

    else:
        cleaned_text = clean_text(email_text)
        email_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(email_vector)[0]

        st.write("### Result")

        if prediction == "spam":
            st.error("Spam")
        else:
            st.success("Not Spam")