# Import necessary Flask modules and external functions
from flask import Flask, render_template, request

# Custom modules for NLP tasks
from preprocessing_words import load_sentiment_dictionary,tokenize_paragraphs,tokenize_words
from review_sentiment import sentence_sentiment,find_most
from sliding_window import sliding_window_sentences,arbitrary_sliding_window
from word_segmentation import word_segmentation,all_segmentations

# Initialize Flask app
app = Flask(__name__)

# --- Flask Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the HTML form
        input_text = request.form.get('text_input', '')
        no_space_text = request.form.get('no_space_input', '').strip().lower()

        # Load sentiment dictionary from file (AFINN format)
        sentiment_dict = load_sentiment_dictionary("afinn.txt")
        dictionary_words = set(sentiment_dict.keys())  # Extract dictionary words for segmentation

        # Sentiment Analysis Part
        # Tokenize the paragraph into sentences
        sentences = tokenize_paragraphs(input_text)
        
        # Calculate sentiment score for each sentence
        sentences_with_scores = [(s, sentence_sentiment(s, sentiment_dict)) for s in sentences]
        #print(type(sentences_with_scores[1]),type(sentences_with_scores))

        # Most positive/negative sentence
        try:
            most_positive = find_most(sentences_with_scores, 1, True)[0] # Highest score
            most_negative = find_most(sentences_with_scores, 1, False)[0] # Lowest score
        except:
            most_positive = ("",0)
            most_negative = ("",0)
        #print(most_positive,type(most_positive))

        # Sliding window segments
        if len(sentences_with_scores) >= 3:
            # Use fixed-size sliding window (size 3) over sentence list
            segments = sliding_window_sentences(sentences_with_scores, 3)
            #print(segments,type(segments),type(segments[1]))
            
            # Get best and worst segments based on sentiment score
            best_segment = find_most(segments, 1, True)[0]
            worst_segment = find_most(segments, 1, False)[0]
            #print(best_segment,type(best_segment))
            
        else:
            # Not enough sentences for sliding window
            best_segment = ([], 0)
            worst_segment = ([], 0)

        # Arbitrary segments (Kadane)
        if sentences_with_scores:
            # Best arbitrary subarray (max sum of sentiment scores)
            best_arbitrary, best_arbitrary_score = arbitrary_sliding_window(sentences_with_scores)
            
            # Worst arbitrary subarray (min sum): apply Kadane's to negative scores, then negate the result
            worst_arbitrary, worst_arbitrary_score = arbitrary_sliding_window([(s, -sc) for s, sc in sentences_with_scores])
            worst_arbitrary_score = -worst_arbitrary_score
        else:
            best_arbitrary = worst_arbitrary = []
            best_arbitrary_score = worst_arbitrary_score = 0

        # Segmentation Part
        one_segmentation = []  # One possible segmentation
        all_segmentations_result = [] # All valid segmentations

        if no_space_text:
            # Perform segmentation on the no-space input using the dictionary
            one_segmentation = word_segmentation(no_space_text, dictionary_words)
            all_segmentations_result = all_segmentations(no_space_text, dictionary_words)
            #print(all_segmentations_result)

        # --- Render the results to the template ---
        return render_template('index.html',
                               sentences=sentences_with_scores,
                               most_positive=most_positive,
                               most_negative=most_negative,
                               best_segment=best_segment,
                               worst_segment=worst_segment,
                               best_arbitrary=(best_arbitrary, best_arbitrary_score),
                               worst_arbitrary=(worst_arbitrary, worst_arbitrary_score),
                               no_space_input=no_space_text,
                               one_segmentation=one_segmentation,
                               all_segmentations=all_segmentations_result)
    # Render the empty form when the request method is GET
    return render_template('index.html')

# --- Run the Flask App ---
if __name__ == '__main__':
    # Run locally on port 8080 with debugging enabled
    app.run(host='127.0.0.1', port=8080, debug=True)