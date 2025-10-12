**Review Sentinment Analysis**

This is the python project for review sentiment analysis as part of INF1002 Programming Fundementals Project.

**Brief description of the project**

This project aims to analyze and classify sentences based on sentiment. The goal is to automatically determine whether a given
text expresses a positive, negative or neutral sentiment.

We built this project because sentiment analysis is a important problem in natural language processing (NLP). It can be applied
in many real-world scenarios, such as understanding customer feedback, analyzing product reviews, or gauging public opinion on
social media. By creating this project, we learned how to preprocess text, apply lexicon-based methods, and design a Python
program that classifies sentiments effectively.

**Features**

- Process input text
- Preprocess module to tokenize / remove stopwords
- Classify sentiment as positive/negative/neutral
- WEB UI to submit reviews

**Architecture**
1. Input Text -> Preprocessing (tokenization, stopwords removal)
2. Lexicon-based scoring using afinn.txt
3. Sliding window / segmentation
4. Output Sentiment label

**Directory**
python-project-G9/

├── templates/index.html #Website
├── tests/test_processing_words.py (Test Case/Edge case for preprocessing_words.py)
├── tests/test_review_sentiment.py (Test Case/Edge case for review_sentiment.py)
├── tests/test_sliding_window.py (Test Case/Edge case for sliding_window.py)
├── tests/test_word_segmentation.py (Test Case/Edge case for word_segmentation.py)
├── flaskcrud.py
├── preprocessing_words.py
├── review_sentiment.py
├── sliding_window.py
├── word_segmentation.py
└── afinn.txt # sentiment lexicon / data file

**Framework**
- Flask (Web Framework)

**How to run**
- python flaskcrud.py

**Demonstrations/Screenshot**
<img width="2518" height="1600" alt="image" src="https://github.com/user-attachments/assets/c50e9763-5a3c-48a5-88ce-311ebae24f88" />

