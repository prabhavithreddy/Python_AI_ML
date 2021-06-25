import string


def is_pangram(sentence):
    alphabets = set(string.ascii_lowercase)
    sentence = set(sentence)
    return alphabets <= sentence


print(is_pangram("The quick brown fox jumps over the lazy dog"))