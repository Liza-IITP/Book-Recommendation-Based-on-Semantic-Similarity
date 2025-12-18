# 📚 Emotion-Aware Book Recommendation System

An end-to-end **NLP-powered recommendation engine** that moves beyond simple keyword matching. This system leverages Transformer models to understand **semantic context**, **broad categorization**, and the **emotional resonance** of book descriptions.

The project concludes with an interactive Gradio dashboard for exploring books based on specific emotional profiles.

---

## 🚀 Project Overview

Standard recommendation systems often rely on genres or authors. This project builds a deeper understanding by analyzing:

* **Semantic Meaning:** Using sentence embeddings to find books with similar themes.
* **Zero-Shot Categorization:** Automatically classifying books into Fiction vs. Non-fiction without manual labeling.
* **Emotion Extraction:** Identifying the core "vibe" of a book (Joy, Sadness, Anger, Fear, Surprise, Disgust, or Neutral).

The heavy NLP computation is performed **offline** to ensure the final user-facing dashboard is fast and responsive.

---

## 🧠 Key Features

* 🔍 **Semantic Search:** Powered by `sentence-transformers` (MiniLM) for context-aware discovery.
* 🏷️ **Zero-Shot Classification:** Categorizes books dynamically using BART-based models.
* 😊 **Emotion Analysis:** Sentence-level emotion extraction aggregated into book-level vectors.
* 📊 **Emotion-Aware Ranking:** Filter and sort books based on emotional intensity.
* 🖥️ **Interactive UI:** A sleek Gradio dashboard for real-time exploration.

---

## 📂 Repository Structure

```text
emotion-aware-book-recommender/
├── code_files/
│   ├── 1_data_preprocessing.ipynb           # Data cleaning & preparation
│   ├── 2_similarity_search_categories.ipynb  # Vector embeddings & classification
│   ├── 3_sentiment_analysis.ipynb           # Emotion extraction pipeline
│   └── 4_dashboard.py                       # Gradio UI application
│
├── data/
│   ├── books_cleaned.csv                    # Initial cleaned dataset
│   ├── books_cleaned_with_categ.csv         # Data + semantic categories
│   └── books_with_emotions.csv              # Final dataset with emotion scores
│
└── README.md
