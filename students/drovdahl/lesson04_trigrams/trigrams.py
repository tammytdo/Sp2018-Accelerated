#! /usr/local/bin/python3


'''
Trigrams Project

Taking a source text file, print a single sentence using the trigrams sequence
of the source file.  Also print a small paragraph.

Play with enumeration of the text in order to achieve the desired results

'''
import random




def parse_file(filename):
    """
    parse text file to make list of words
    """
    words = []
    with open(filename) as infile:
        for _ in range(61):
            infile.readline()
        for line in infile:
            if line.startswith("End of the Project Gutenberg"):
                break
            wrds = line.strip().split()
            words.extend(wrds)
    return words


def build_trigram(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        pair = (first, second)

        list_of_followers = tris.setdefault(pair, [])
        list_of_followers.append(third)

        # if pair in tris:
        #     list_of_followers = tris[pair]
        # else:
        #     list_of_followers = tris[pair] = []
        # list_of_followers.append(third)

    return tris


def make_new_text(trigram):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(20):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    print(sentence)
    return sentence


def make_new_text2(trigram):
    # start the new text with a random, 'Capital' word (key)
    # if the random key does not start with a capital letter, then get another
    # different random key
    #
    # establish the end of sentence character
    e = ('.', '?', '!')
    pair = random.choice(list(trigram.keys()))
    while True:
        if not pair[0].istitle():
            pair = random.choice(list(trigram.keys()))
        else:
            break
    sentence = []
    sentence.extend(pair)
    # if first two words of sentence end with '.', return the sentence
    if sentence[1].strip('"').endswith(e) and sentence[1].strip('"') != 'Mr.':
        return sentence
    # if the first word of the sentence ends with '.', start over
    if sentence[0].strip('"').endswith(e):
        return make_new_text2(trigram)
    # build on the sentence and end it when a '.' is returned from the random
    # function
    for i in range(30):
        followers = trigram[pair]
        end_word_match = False
        # try to end the sentence is longer than 15 words by influencing the
        # choice of the 'random' function
        if i > 15:
            # will check random responses up to 10 times for words that end
            # with a '.'
            # if found, the word with a '.' at the end will be selected
            # if not found, continue on and repeat until a '.' is found
            # if the i finally gets to 30 without finding a '.', there will
            # not be a complete sentence
            for x in range(10):
                end_word_search = random.choice(followers)
                if end_word_search.strip('"').endswith(e) and end_word_search != 'Mr.':
                    sentence.append(end_word_search)
                    end_word_match is True
                    return sentence
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
        if pair[1].strip('"').endswith(e) and pair[1].strip('"') != 'Mr.':
            break
    return sentence


if __name__ == "__main__":
    words = parse_file("sherlock.txt")
    trigram = build_trigram(words)
    text = make_new_text2(trigram)
    # print sentence
    for word in text:
        print(word.strip('"\''), end=' ')
    print('\n\n')
    # print paragraph with 5 sentences
    for i in range(5):
            text = make_new_text2(trigram)
            for word in text:
                print(word.strip('"\''), end=' ')
