import pandas as pd

df = pd.read_csv("dataset.csv")

print("Dataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate emails:")
print(df["text"].duplicated().sum())

print("\nClass distribution:")
print(df["label"].value_counts())

print("\nEmail length:")
print(df["text"].str.len().describe())