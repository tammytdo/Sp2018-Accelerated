#!/usr/bin/env python3
import sys
import random


def read_book(infilename):
    """
    Return the contents of the file as one string
    """
    with open(infilename, 'r') as infile:
        # strip out the header, table of contents, etc.
        for i in range(44):
            infile.readline()

        full_text = []
        for line in infile:
            if line.startswith("End of the Project Gutenberg EBook"):
                break
            full_text.append(line)

    return " ".join(full_text)


def clean_words(text):
    """Strip unwanted punctuation from a large string and return a list of word"""

    replace_punc = [('-', ''),
                    (',', ''),
                    (',', ''),
                    ('.', ''),
                    (')', ''),
                    ('(', ''),
                    ('"', '')]

    # Create a translation table for str.translate to utilize
    table = {}
    for og, replace in replace_punc:
        table[ord(og)] = replace
    text = text.translate(table).lower()

    # Cast all characters to lowercase to eliminate lowercase/uppercase duplicates
    text = text.lower()

    # Split into words
    words = text.split()

    # Remove bare single quote and replace "i" with "I"
    words2 = []
    [words2.append("I" if word == "i" else word) for word in words if word != "'"]
    return words2


def build_trigram(words):
    """Build a trigram dictionary from the words in the string output from read_book.
       Keys = word pairs
       Values = list of words that follow each pair
    """

    word_pairs = {}

    for i in range(len(words) - 2):  # Need a pair
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        word_pairs.setdefault(pair, []).append(follower)

    return word_pairs


def build_book(word_pairs):

    """
    Build a new book with the trigram pairs. Add sentences back in.
    """

    new_text = []
    for i in range(10):  # do ten sentences
        # pick a word pair to start the sentence
        # need to make dict.keys() a list to randomly select from it
        sentence = list(random.choice(list(word_pairs.keys())))
        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])  # the next word pair is the last two words
            sentence.append(random.choice(word_pairs[pair]))

        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()

        # Add the period
        sentence[-1] += "."
        new_text.extend(sentence)

    new_text = " ".join(new_text)

    return new_text


if __name__ == "__main__":

    in_data = read_book("Through_Looking_glass.txt")
    words = clean_words(in_data)
    word_pairs = build_trigram(words)
    new_book = build_book(word_pairs)

    print(new_book)