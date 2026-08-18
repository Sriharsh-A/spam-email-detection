import re
import joblib
import pandas as pd

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


test_emails = [
    "Congratulations! You have won a free iPhone. Click here to claim your prize.",
    "You have been selected for a cash reward. Claim your money immediately.",
    "URGENT! Your account has been selected for a special bonus. Click the link now.",
    "Hi, please find the project report attached. Let me know if any changes are required.",
    "The meeting has been moved to 3 PM tomorrow. Please be available.",
    "Please grant me leave tomorrow as I have a family function.",
    "Happy birthday! We are having a small celebration at home. You are invited.",
    "Your electricity bill is due tomorrow. Please make the payment through the official portal.",
    "Win a luxury car by entering this lucky draw. Register now!",
    "Can you send me the notes from today's class?"
]

results = []

for i, email in enumerate(test_emails, 1):
    cleaned_text = clean_text(email)
    email_vector = vectorizer.transform([cleaned_text])
    prediction = model.predict(email_vector)[0]

    results.append({
        "test_number": i,
        "email": email,
        "prediction": prediction
    })

    print(f"\nTest {i}")
    print("Email:", email)
    print("Prediction:", prediction.upper())

results_df = pd.DataFrame(results)

results_df.to_csv("test_results.csv", index=False)

print("\nTest results saved as test_results.csv")