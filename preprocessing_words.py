import re

def load_sentiment_dictionary(path: str):
    sentiment_dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            word, score = line.strip().split('\t')
            sentiment_dict[word.lower()] = int(score)
    return sentiment_dict


def tokenize_paragraphs(text):
    paragraphs = [p.strip() for p in text.strip().split('\n') if p.strip()]
    paragraph_sentences = []
    for p in paragraphs:
        sentences = re.split(r'(?<=[.!?])\s+', p)
        paragraph_sentences.extend(sentences)
    return paragraph_sentences

def tokenize_words(sentence):
    return re.findall(r'\b\w+\b', sentence.lower())
