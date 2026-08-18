import re
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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


email_text = input("\nEnter email text:\n")

cleaned_text = clean_text(email_text)

email_vector = vectorizer.transform([cleaned_text])

prediction = model.predict(email_vector)[0]

if prediction == "spam":
    print("\nResult: SPAM")
else:
    print("\nResult: NOT SPAM")