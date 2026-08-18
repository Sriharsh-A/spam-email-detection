import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

counts = df["label"].value_counts()

labels = ["Ham", "Spam"]
values = [
    counts.get("ham", 0),
    counts.get("spam", 0)
]

plt.figure(figsize=(7, 5))

bars = plt.bar(labels, values)

plt.title("Distribution of Ham and Spam Emails")
plt.xlabel("Email Type")
plt.ylabel("Number of Emails")

for bar, value in zip(bars, values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 50,
        str(value),
        ha="center"
    )

plt.tight_layout()
plt.savefig("email_distribution.png", dpi=300)
plt.show()