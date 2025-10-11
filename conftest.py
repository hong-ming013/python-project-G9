# tests/conftest.py
import pytest

@pytest.fixture
def sample_text():
    # Sample input string used for sentiment tests
    return "I absolutely love this phone, but the battery is bad."

@pytest.fixture
def tiny_afinn():
    # Minimal sentiment lexicon for isolated tests
    # Keys are words, values are sentiment scores
    return {"love": 3, "bad": -2, "absolutely": 0, "battery": 0, "phone": 0}