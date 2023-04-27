import random
from dictionary import dictionary
from project import start_learning, generate_random_word, get_translation, get_options


def test_generate_random_word():
    word = generate_random_word()
    assert word in dictionary.keys()


def test_get_translation():
    word = random.choice(list(dictionary.keys()))
    translation = get_translation(word)
    assert translation == dictionary[word]


def test_get_options():
    translation = random.choice(list(dictionary.values()))
    num_options = 4
    options = get_options(translation, num_options)
    assert len(options) == num_options
    assert translation in options


def test_start_learning(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    start_learning('2', get_input=lambda _: '2')




if __name__ == "__main__":
    test_generate_random_word()
    test_get_translation()
    test_get_options()
    test_start_learning()