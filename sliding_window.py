def sliding_window_sentences(sentences_with_scores, window_size=3):
    segments = []
    for i in range(len(sentences_with_scores) - window_size + 1):
        window = sentences_with_scores[i:i+window_size]
        texts = [s[0] for s in window]
        score = sum(s[1] for s in window)
        segments.append((texts, score))
    return segments

def arbitrary_sliding_window(sentences):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0

    for i, (sentence, score) in enumerate(sentences):
        if current_sum <= 0:
            current_sum = score
            temp_start = i
        else:
            current_sum += score

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    best_segment = [s[0] for s in sentences[start:end+1]]
    print(best_segment, max_sum)
    return best_segment, max_sum
