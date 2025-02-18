import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                                     get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)
from unittest.mock import patch

def test_get_seven_letter_word():
    with patch('builtins.input', return_value='elephant'):  # Mock user input to 'elephant'
        result = get_seven_letter_word()
        assert result == 'ELEPHANT'  # Expected output is the uppercase form of 'elephant'

def test_parse_json_from_file(tmp_path):
    data = {"key": "value"}
    file = tmp_path / "test.json"
    with open(file, "w") as f:
        json.dump(data, f)

    result = parse_json_from_file(file)
    assert result == data

def test_choose_sentence_structure():
    result = choose_sentence_structure()
    assert result in structures  # Assuming structures is a list of valid structures

def test_get_pronoun():
    result = get_pronoun()
    assert result in ["he", "she", "they", "it", "we"]  # Include 'we' as a possible pronoun

def test_get_article():
    result = get_article()
    assert result in ["a", "the"]

def test_get_word():
    letter = "A"  # A single letter as a string
    word_list = ["apple", "banana", "cherry"]
    result = get_word(letter, word_list)
    assert result == "apple"  # Expecting the word corresponding to the letter 'A'

def test_fix_agreement():
    sentence = ["he", "quickly", "go", "to", "school"]  # "go" should become "goes"
    fix_agreement(sentence)
    assert sentence == ["he", "quickly", "goes", "to", "school"]  # Check if verb is updated correctly

def test_build_sentence():
    seed_word = "abcdefg"  # 7-letter word
    structure = ["PRO", "ADV", "VERB", "ART", "ADJ", "NOUN"]
    data = {
        "adjectives": ["quick", "lazy", "happy"],
        "nouns": ["dog", "cat", "mouse"],
        "verbs": ["runs", "jumps", "chases"],
        "adverbs": ["quickly", "slowly", "gracefully"],
        "prepositions": ["on", "under", "over"]
    }
    result = build_sentence(seed_word, structure, data)
    print("Generated Sentence:", result)
    assert result.startswith("He quickly")  # Accepts any of the verbs (e.g., 'jumps', 'chases', 'runs')
    assert "dog" in result  # Ensures a noun ("dog") is in the sentence