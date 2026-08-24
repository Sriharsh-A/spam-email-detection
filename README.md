# Spam Email Detector

A machine learning project that classifies email messages as **Spam** or **Not Spam** using Natural Language Processing and Machine Learning.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NLP](https://img.shields.io/badge/NLP-NLTK-orange)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-red)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b)

</p>

---

## Overview

This project analyzes the text of an email and predicts whether it belongs to the **Spam** or **Ham (Not Spam)** category.

The system uses:

**Text Preprocessing → TF-IDF → Multinomial Naive Bayes → Prediction**

A Streamlit web interface is also provided for testing individual email messages.

---

## Features

- Email dataset loading and exploration
- Text preprocessing using NLTK
- TF-IDF feature extraction
- Multinomial Naive Bayes classification
- Model evaluation
- Confusion matrix
- Dataset visualization
- Streamlit web application
- Manual email testing

---

## Model Performance

The model was evaluated on **1,187 test emails**.

| Metric | Score |
|---|---:|
| Accuracy | **96.29%** |
| Spam Precision | **92%** |
| Spam Recall | **96%** |
| Spam F1-Score | **94%** |

### Confusion Matrix

```text
[[802  28]
 [ 16 341]]

The model correctly classified 341 of 357 spam emails in the test set.

Dataset
Category	Number of Emails
Ham	4,151
Spam	1,898
Total	6,049

The raw dataset and generated CSV files are excluded from the GitHub repository.

Tech Stack
Python
Pandas
NLTK
Scikit-learn
Matplotlib
Joblib
Streamlit
Project Structure
Spam_Email_Detection/
│
├── model/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── load_dataset.py
│   ├── explore_dataset.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│   ├── evaluate_model.py
│   ├── visualize_dataset.py
│   └── test_predictions.py
│
├── app.py
├── confusion_matrix.png
├── email_distribution.png
├── test_results.csv
├── requirements.txt
├── .gitignore
└── README.md
Run the Project

Create and activate a virtual environment:

python -m venv venv

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py
Limitations

The model performs well on the evaluation dataset but may misclassify short or unusual messages that differ significantly from the training data.

It is a spam classification system, not a complete phishing or malicious-website detection system.

Future Scope
Use larger and more diverse email datasets
Compare different machine learning algorithms
Improve text feature extraction
Handle HTML emails
Incorporate email headers and metadata
Improve phishing-related email detection