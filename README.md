# 📊 Reddit Sentiment Analysis (February 2025 Data)

This project analyzes the sentiment of Reddit comments collected in February 2025 from a wide range of subreddits spanning technology, finance, lifestyle, and more. The goal is to understand public opinion and community sentiment at scale using advanced NLP techniques.

---

## 🌐 Subreddit Topics Covered

A diverse set of domains and interests:

- **Technology**: Cybersecurity, Quantum Computing, Space, Engineering
- **Finance**: Stocks, CryptoCurrency, wallstreetbets, Economy, Investing, Business, PersonalFinance, RealEstate, SideHustle, Ecommerce
- **Lifestyle & Productivity**: Productivity, Minimalism, Stoicism, Fitness, Cooking
- **Creative & DIY**: Photography, DIY, Writing
- **Travel**: Travel
- ... and many more

---

## 🧠 Approach

We compare two different sentiment analysis methodologies:

1️⃣ **BERT (Bidirectional Encoder Representations from Transformers)**
- State-of-the-art deep learning transformer model
- Fine-tuned on the labeled Reddit dataset
- Captures context and nuance in user-generated language

2️⃣ **Naive Bayes Classifier**
- Classical machine learning approach
- Uses TF-IDF features for representing text
- Serves as a strong baseline for comparison

---

## ⚙️ Workflow Overview

- **Data Collection**: Scraped Reddit comments from February 2025 across various subreddits to capture diverse opinions
- **Preprocessing**: Text cleaning, tokenization, lowercasing, stop-word removal
- **Labeling**: Annotated each comment for sentiment (positive, negative, neutral)
- **Model Training**:
  - Fine-tuned BERT on the labeled data
  - Trained Naive Bayes using TF-IDF feature vectors
- **Evaluation**:
  - Compared model performance using accuracy, precision, recall, and F1-score
  - Analyzed misclassifications to understand strengths and weaknesses

---

## 🎯 Results & Insights

- **BERT outperformed Naive Bayes** across all evaluation metrics
- Demonstrated the effectiveness of modern NLP models in handling noisy, real-world, user-generated content
- Highlighted how transformer-based approaches better capture contextual sentiment compared to traditional bag-of-words methods

---

## ✅ Key Takeaways

- Sentiment analysis of Reddit data provides valuable insights into community opinions on a wide range of topics
- Fine-tuning BERT significantly improves classification performance over classical machine learning methods
- Combining modern deep learning with traditional techniques offers a robust framework for text analytics on social media data

---

## 📌 Project Goals

- Enable large-scale sentiment analysis of diverse Reddit discussions
- Compare classical and modern NLP approaches on real-world social media text
- Provide an open-source, reproducible framework for Reddit sentiment research

---

## 🚀 Technologies Used

- Python
- Transformers (Hugging Face BERT)
- Scikit-learn (Naive Bayes, TF-IDF)
- Pandas, NumPy
- Matplotlib for visualization

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request if you'd like to help improve this project.

