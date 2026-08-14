import os
import pandas as pd

ham_path = "../dataset/ham"
spam_path = "../dataset/spam"

emails = []
labels = []

for filename in os.listdir(ham_path):
    file_path = os.path.join(ham_path, filename)

    try:
        with open(file_path, "r", encoding="latin-1") as file:
            emails.append(file.read())
            labels.append("ham")
    except:
        pass

for filename in os.listdir(spam_path):
    file_path = os.path.join(spam_path, filename)

    try:
        with open(file_path, "r", encoding="latin-1") as file:
            emails.append(file.read())
            labels.append("spam")
    except:
        pass

df = pd.DataFrame({
    "text": emails,
    "label": labels
})

print("Dataset loaded successfully!")
print("Total emails:", len(df))
print("\nClass distribution:")
print(df["label"].value_counts())

print("\nFirst 5 records:")
print(df.head())