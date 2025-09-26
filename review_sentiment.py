import copy
from preprocessing_words import tokenize_words

def sentence_sentiment(sentence, sentiment_dict):
    words = tokenize_words(sentence)
    return sum(sentiment_dict.get(word, 0) for word in words)

def find_most(word_scores, n, positive):
    items = copy.deepcopy(word_scores)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if positive:
                if (items[i][1] < items[j][1]):
                    items[i], items[j] = items[j], items[i]
                elif items[i][1] == items[j][1]:
                    if items[i][0] > items[j][0]:
                        items[i], items[j] = items[j], items[i]
            else:
                if (items[i][1] > items[j][1]):
                    items[i], items[j] = items[j], items[i]
                elif items[i][1] == items[j][1]:
                    if items[i][0] > items[j][0]:
                        items[i], items[j] = items[j], items[i]
    return items[:n]
