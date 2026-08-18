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