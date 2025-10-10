import copy
from preprocessing_words import tokenize_words

# --- Function: Calculate sentiment score of a sentence ---
def sentence_sentiment(sentence, sentiment_dict):
    # Tokenize sentence into individual words
    words = tokenize_words(sentence)
    
    # Calculate total sentiment score by summing the scores of individual words
    # If a word is not in the dictionary, default to 0
    return sum(sentiment_dict.get(word, 0) for word in words)

# --- Function: Find top n most positive or negative items ---
# word_scores: list of tuples (sentence, score)
# n: number of top results to return
# positive: True for most positive, False for most negative
def find_most(word_scores, n, positive):
    # Create a deep copy to avoid modifying the original list
    items = copy.deepcopy(word_scores)
    
    # Custom sort: nested loop to compare each pair of elements
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if positive:
                # If sorting for positive sentiment
                if (items[i][1] < items[j][1]):
                    items[i], items[j] = items[j], items[i] # Swap if item j is more positive
                elif items[i][1] == items[j][1]:
                    # If scores are equal, sort alphabetically (ascending)
                    if items[i][0] > items[j][0]:
                        items[i], items[j] = items[j], items[i]
            else:
                # If sorting for negative sentiment
                if (items[i][1] > items[j][1]):
                    items[i], items[j] = items[j], items[i] # Swap if item j is more negative
                elif items[i][1] == items[j][1]:
                    # If scores are equal, sort alphabetically (ascending)
                    if items[i][0] > items[j][0]:
                        items[i], items[j] = items[j], items[i]

    # Return the top n items after sorting
    return items[:n]

