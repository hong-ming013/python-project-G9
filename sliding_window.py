# --- Function: Sliding window over sentence scores (fixed size) ---
def sliding_window_sentences(sentences_with_scores, window_size=3):
    segments = []

    # Slide a window of 'window_size' over the list of sentences
    for i in range(len(sentences_with_scores) - window_size + 1):
        # Extract a window of consecutive sentences
        window = sentences_with_scores[i:i+window_size]

        # Extract just the sentence texts from the window
        texts = [s[0] for s in window]

        # Calculate the total sentiment score for the window
        score = sum(s[1] for s in window)

        # Store the window (as a list of sentences) and its score as a tuple
        segments.append((texts, score))

    # Return the list of (segment, score) tuples
    return segments

# Finding the best arbitrary-length segment using Kadane Algorithm
def arbitrary_sliding_window(sentences):
    max_sum = float('-inf')  # Maximum score found so far
    current_sum = 0          # Current running total
    start = end = temp_start = 0  # Indices to track best segment

    # Iterate through each sentence and its sentiment score
    for i, (sentence, score) in enumerate(sentences):
        # If current sum is negative or zero, reset it at current index
        if current_sum <= 0:
            current_sum = score
            temp_start = i
        else:
            # Otherwise, add current score to the running total
            current_sum += score

        # Update max_sum and track indices if new max is found
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    # Extract only the sentence texts from the best segment
    best_segment = [s[0] for s in sentences[start:end+1]]

    # Debug print (can be removed in production)
    print(best_segment, max_sum)

    # Return the best segment and its total sentiment score
    return best_segment, max_sum
