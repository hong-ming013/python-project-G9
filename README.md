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
<img width="1920" height="1758" alt="Screencapture" src="https://github.com/user-attachments/assets/9eb73ecf-c0ff-4901-91c0-0b5ddc4a49ab" />
