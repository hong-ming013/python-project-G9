import re

# --- Load sentiment dictionary from file ---
def load_sentiment_dictionary(path: str):
    sentiment_dict = {}

    # Open the file containing sentiment words and scores (e.g., afinn.txt)
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            # Each line is expected to be in the format: word<TAB>score
            word, score = line.strip().split('\t')

            # Store word and its sentiment score (converted to integer) in dictionary
            sentiment_dict[word.lower()] = int(score)

    # Return the sentiment dictionary
    return sentiment_dict

# --- Tokenize paragraphs into sentences ---
def tokenize_paragraphs(text):
    # List of known abbreviations to avoid incorrect sentence splitting
    abbreviations = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'St.', 'Sr.', 'Jr.', 'vs.', 'Prof.', 'Inc.', 'Pte.', 'Ltd.', 'e.g.', 'i.e.', 'etc.']

    # Regex pattern to split sentences after '.', '?', or '!' if followed by whitespace or capital letter
    sentence_split_pattern = r'(?<=[.!?])(?=\s+|[A-Z])'

    # Split text into non-empty paragraphs by newline
    paragraphs = [p.strip() for p in text.strip().split('\n') if p.strip()]
    paragraph_sentences = []

    # Process each paragraph
    for p in paragraphs:
        # Split paragraph into raw sentences using regex
        raw_sentences = re.split(sentence_split_pattern, p)
        cleaned_sentences = []

        buffer = '' # Buffer to handle abbreviations and merge wrongly split sentences
        for sentence in raw_sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            # Check if current sentence ends with any abbreviation
            is_abbrev = any(sentence.endswith(abbrev) for abbrev in abbreviations)

            # Accumulate sentence in buffer (for abbreviation merging)
            if buffer:
                buffer += ' ' + sentence
            else:
                buffer = sentence

            # If not an abbreviation, finalize the sentence and reset buffer
            if not is_abbrev:
                cleaned_sentences.append(buffer.strip())
                buffer = ''

        # In case buffer has remaining sentence
        if buffer:
            cleaned_sentences.append(buffer.strip())

        # Add all cleaned sentences from this paragraph to result list
        paragraph_sentences.extend(cleaned_sentences)

    # Return list of all sentences
    return paragraph_sentences

# --- Tokenize a sentence into lowercase words ---
def tokenize_words(sentence):
    # Use regex to find word boundaries and convert everything to lowercase
    return re.findall(r'\b\w+\b', sentence.lower())
