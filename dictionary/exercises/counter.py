# Define a function to count the frequency of words in a given list of words.
from collections import defaultdict, Counter


def count_word_frequency(words: list[str]) -> dict[str, int]:
    counter: dict[str, int] = defaultdict(int)
    for word in words:
        counter[word] += 1
    return dict(counter)


def count_word_frequency_with_counter(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))


words = ["apple", "orange", "banana", "apple", "orange", "apple"]
print(count_word_frequency(words))
print(count_word_frequency_with_counter(words))
