def sliding_window_sentences(sentences_with_scores, window_size=3):
    segments = []
    for i in range(len(sentences_with_scores) - window_size + 1):
        window = sentences_with_scores[i:i+window_size]
        texts = [s[0] for s in window]
        score = sum(s[1] for s in window)
        segments.append((texts, score))
    return segments

def arbitrary_sliding_window(sentences):
    max_sum = current_sum = sentences[0][1]
    start = end = temp_start = 0

    for i in range(1, len(sentences)):
        if current_sum < 0:
            current_sum = sentences[i][1]
            temp_start = i
        else:
            current_sum += sentences[i][1]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    best_segment = [s[0] for s in sentences[start:end+1]]
    return best_segment, max_sum
