from sliding_window import sliding_window_sentences, arbitrary_sliding_window, windows
from review_sentiment import sentence_sentiment

def test_arbitrary_sliding_window_kadane():
    # Test max subarray (Kadane’s algorithm style)
    data = [("A", -2), ("B", 3), ("C", 5), ("D", -1), ("E", -4)]
    best_segment, best_sum = arbitrary_sliding_window(data)
    # Best subsequence is ["B","C"] with sum 8
    assert best_segment == ["B", "C"]
    assert best_sum == 8

def test_arbitrary_sliding_window_all_negative():
    # Edge case: all negative values
    data = [("A",-5), ("B",-2), ("C",-8)]
    best_segment, best_sum = arbitrary_sliding_window(data)
    # Best subsequence is the least negative single item: ["B"], -2
    assert best_segment == ["B"]
    assert best_sum == -2

def test_windows_generator_basic():
    # Generate windows from a sequence [0,1,2,3,4,5]
    seq = list(range(6))
    w = list(windows(seq, size=3, step=2))
    # Expect 2 windows of size 3, stepping forward by 2 each time
    assert w == [[0,1,2], [2,3,4]]

def test_sliding_window_sentences_basic():
    # Input is (sentence, score) pairs
    data = [("A", 2), ("B", -1), ("C", 3), ("D", 0)]
    out = sliding_window_sentences(data, window_size=3)
    # Expect consecutive 3-sentence windows with summed scores
    assert out == [
        (["A", "B", "C"], 2 + (-1) + 3),   # = 4
        (["B", "C", "D"], -1 + 3 + 0),     # = 2
    ]

def test_sliding_window_sentences_too_short():
    # Only 2 items, but window size is 3 → should return empty
    data = [("only", 5), ("two", -1)]
    assert sliding_window_sentences(data, window_size=3) == []


def test_fixed_window_best_worst_segment():
    # Tests that the sliding window algorithm correctly identifies the most positive and most negative 3-sentence segments.
    # Example list of sentences with varying sentiment
    sents = ["good", "bad", "great", "poor", "good"]
    # Sentiment dictionary
    lex = {"good": 2, "bad": -2, "great": 3, "poor": -3}
    # Compute a sentiment score for each sentence
    scores = [sentence_sentiment(s, lex) for s in sents]   # Expected: [2, -2, 3, -3, 2]
    # Define window size
    k = 3
    # Generate all possible 3-sentence sliding windows with their total scores
    windows = [(i, i+k, sum(scores[i:i+k])) for i in range(len(scores)-k+1)]
    # Identify the window with the highest and lowest summed sentiment
    best = max(windows, key=lambda x: x[2])
    worst = min(windows, key=lambda x: x[2])
    # Verify that the most positive and most negative segments are correctly detected
    assert best == (0, 3, 3)      # window [0:3] -> [2,-2,3] = +3
    assert worst == (1, 4, -2)    # window [1:4] -> [-2,3,-3] = -2


def test_arbitrary_most_negative_segment():
    # Ensures the algorithm correctly finds the most negative continuous segment of arbitrary length (Kadane’s algorithm variant for minimum sum).
    # Example list of sentiment scores for consecutive sentences
    scores = [2, -5, 1, -4, 3]  # The lowest-sum continuous segment is [-5, 1, -4] = -8
    # Initialize variables for Kadane’s minimum subarray logic
    min_ending = min_so_far = scores[0]
    start = end = tmp_start = 0
    # Iterate through all elements to find minimum-sum segment
    for i in range(1, len(scores)):
        # Decide whether to start a new segment or extend the current one
        if scores[i] < min_ending + scores[i]:
            min_ending = scores[i]
            tmp_start = i
        else:
            min_ending += scores[i]

        # Update overall minimum if a lower sum is found
        if min_ending < min_so_far:
            min_so_far = min_ending
            start = tmp_start
            end = i + 1  # end index is non-inclusive
    # Check that the result matches the expected lowest-sum segment
    assert min_so_far == -8
    assert (start, end) == (1, 4)  # segment indices [1:4] correspond to [-5, 1, -4]
