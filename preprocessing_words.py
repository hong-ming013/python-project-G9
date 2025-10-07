import re

def load_sentiment_dictionary(path: str):
    sentiment_dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            word, score = line.strip().split('\t')
            sentiment_dict[word.lower()] = int(score)
    return sentiment_dict

def tokenize_paragraphs(text):
    abbreviations = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'St.', 'Sr.', 'Jr.', 'vs.', 'Prof.', 'Inc.', 'Pte.', 'Ltd.', 'e.g.', 'i.e.', 'etc.']

    sentence_split_pattern = r'(?<=[.!?])(?=\s+|[A-Z])'

    paragraphs = [p.strip() for p in text.strip().split('\n') if p.strip()]
    paragraph_sentences = []

    for p in paragraphs:
        raw_sentences = re.split(sentence_split_pattern, p)
        cleaned_sentences = []

        buffer = ''
        for sentence in raw_sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            is_abbrev = any(sentence.endswith(abbrev) for abbrev in abbreviations)

            if buffer:
                buffer += ' ' + sentence
            else:
                buffer = sentence

            if not is_abbrev:
                cleaned_sentences.append(buffer.strip())
                buffer = ''

        if buffer:
            cleaned_sentences.append(buffer.strip())

        paragraph_sentences.extend(cleaned_sentences)

    return paragraph_sentences

def tokenize_words(sentence):
    return re.findall(r'\b\w+\b', sentence.lower())
