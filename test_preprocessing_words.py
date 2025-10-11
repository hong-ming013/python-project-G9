from preprocessing_words import tokenize_words as preprocess_text 
from preprocessing_words import tokenize_paragraphs                
from review_sentiment import sentence_sentiment                    

# ------------------------------------------------------
# 1. TOKENIZATION TESTS (tokenize_words)
# ------------------------------------------------------

def test_basic_sentence():
    """
    Test that a normal sentence is correctly tokenized:
    - Words are lowercased
    - Punctuation is removed
    - Output is a clean list of tokens
    """
    assert preprocess_text("I love this phone!") == ["i", "love", "this", "phone"]

def test_symbols_and_numbers():
    """
    Test that:
    - Numbers are preserved
    - Special symbols ($, !, etc.) are removed
    - Text is cleaned and normalized
    """
    assert preprocess_text("123 $$$ Great!!!") == ["123", "great"]

def test_empty_string():
    """
    Test that an empty string input returns an empty list of tokens.
    This verifies the function handles blank input gracefully.
    """
    assert preprocess_text("") == []

def test_case_insensitivity():
    """
    Test that mixed-case words are normalized to lowercase.
    Ensures tokenization is not case-sensitive.
    """
    assert preprocess_text("BaTtErY") == ["battery"]

def test_whitespace_only():
    """
    Test that strings with only whitespace characters
    (spaces, tabs, or newlines) return an empty token list.
    """
    assert preprocess_text("   \t \n  ") == []

def test_punctuation_only():
    """
    Test that a string containing only punctuation marks
    returns an empty token list, since no valid words exist.
    """
    assert preprocess_text("!!!???.,;") == []

def test_non_string_input_is_handled():
    """
    Test that non-string inputs (e.g., integers) are handled safely.
    The function should cast the input to a string before processing.
    """
    assert preprocess_text(12345) == ["12345"]

# ------------------------------------------------------
# 2. PARAGRAPH & SENTENCE SPLITTING TESTS (tokenize_paragraphs)
# ------------------------------------------------------

def test_sentence_split_basic_and_newlines():
    """
    Test that multi-line input text is split into sentences correctly.
    - Each sentence ends with '.', '!', or '?'
    - Newlines are treated as paragraph breaks
    """
    text = "Good phone. Terrible battery life!\nOkay camera?"
    out = tokenize_paragraphs(text)
    assert out == ["Good phone.", "Terrible battery life!", "Okay camera?"]

def test_sentence_split_empty_and_whitespace():
    """
    Test that empty or whitespace-only text returns an empty list.
    This ensures the sentence splitter ignores blank paragraphs.
    """
    assert tokenize_paragraphs("   \n \t ") == []

# ------------------------------------------------------
# 3. SENTIMENT ANALYSIS TESTS (sentence_sentiment)
# ------------------------------------------------------

def test_sentence_sentiment_with_custom_dict():
    """
    Test sentiment score computation using a custom mini-dictionary.
    - Positive word ('good') adds +3
    - Negative word ('bad') adds -2
    - Neutral word ('phone') adds 0
    Ensures total sentiment score sums correctly.
    """
    lex = {"good": 3, "bad": -2, "phone": 0}
    assert sentence_sentiment("good phone", lex) == 3
    assert sentence_sentiment("bad phone", lex) == -2
    assert sentence_sentiment("average phone", lex) == 0