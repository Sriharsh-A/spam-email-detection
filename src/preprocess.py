import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_csv("dataset.csv")

stop_words = set(stopwords.words("english"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


df["clean_text"] = df["text"].apply(clean_text)

print("Text preprocessing completed!")

print("\nOriginal email:")
print(df["text"].iloc[0][:500])

print("\nCleaned email:")
print(df["clean_text"].iloc[0][:500])

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")