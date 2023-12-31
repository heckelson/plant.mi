import random as rand
from functools import cache


@cache
def __get_words():
    with open("app/static/words.txt") as file:
        return [word.replace("\n", "").lower() for word in file.readlines()]


def generate_username() -> str:
    words = __get_words()
    return "-".join(rand.sample(words, 2)).lower()


def generate_password() -> str:
    words = __get_words()
    return "-".join(rand.sample(words, 4)).lower()
