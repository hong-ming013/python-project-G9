from word_segmentation import word_segmentation, all_segmentations

def test_simple_segmentation():
    # Checks correct splitting using known dictionary entries (e.g., 'goodphone' → 'good phone').
    dictionary = {"good", "phone"}
    assert word_segmentation("goodphone", dictionary) == "good phone"

def test_word_not_in_dictionary():
    # Ensures function returns empty string when segmentation is invalid.
    dictionary = {"good", "camera"}
    assert word_segmentation("cameron", dictionary) == ""

def test_empty_input_word_segmentation():
    # Verifies that empty input returns an empty string safely.
    dictionary = {"a", "b"}
    assert word_segmentation("", dictionary) == ""

def test_all_segmentations_no_solution_returns_empty_string_list():
    # Confirms all_segmentations() returns [''] when no segmentation is possible.
    dictionary = {"good", "phone", "battery"}
    res = all_segmentations("xyz", dictionary)
    assert res == [""]

def test_single_valid_segmentation_all_segmentations():
    # Tests one valid segmentation ('goodphone' → 'good phone').
    dictionary = {"good", "phone"}
    res = all_segmentations("goodphone", dictionary)
    assert sorted(res) == sorted(["good phone"])

def test_multiple_segmentations_overlapping_words():
    # Ensures overlapping words ('a','aa','aaa') produce all valid segmentations.
    dictionary = {"a", "aa", "aaa"}
    res = all_segmentations("aaaa", dictionary)
    expected = [
        "a a a a", "aa a a", "a aa a", "a a aa",
        "aa aa", "aaa a", "a aaa",
    ]
    assert sorted(res) == sorted(expected)

def test_empty_input_all_segmentations():
    # Checks empty input returns [''] without error.
    dictionary = {"anything"}
    res = all_segmentations("", dictionary)
    assert res == [""]

def test_empty_dictionary_all_segmentations():
    # Ensures empty dictionary returns [''] instead of crashing.
    dictionary = set()
    res = all_segmentations("anything", dictionary)
    assert res == [""]
