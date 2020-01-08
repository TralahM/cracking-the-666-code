import string
import random

LETTERS = list(string.ascii_uppercase)
INDEX = [i*6 for i in range(1, 27)]
MAPPING = dict(zip(LETTERS, INDEX))


def score_word(word):
    global MAPPING
    lookup = list(word.upper())
    score = sum([MAPPING[k] for k in lookup])
    return word, score


def random_word_scoring(score=6):
    global LETTERS
    for i in range(1, 26):
        rwd = random.sample(LETTERS, i)
        print(score_word(rwd))
