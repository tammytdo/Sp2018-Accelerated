import random

#reading in a text file
inputfile = open('sherlock_small.txt')
novel = inputfile.read()
inputfile.close()

# Builds the dicitonary with which the Kata is built
def dictionary_builder(text):
    words = text.replace('\n', ' ').split(' ')
    trigrams = {}
    for i, word in enumerate(words):
        if i == (len(words) - 2):
            break
        elif words[i] + ' ' + words[i + 1] not in trigrams:
            trigrams[words[i] + ' ' + words[i + 1]] = [words[i + 2]]
        else:
            trigrams[words[i] + ' ' + words[i + 1]].append(words[i + 2])
    return trigrams


def random_trigram(list):
    return random.choice(list)


def text_generator(text, start, num_words = 10):
    trigrams = dictionary_builder(text)
    if start not in trigrams:
        print('The phrase you provided doesn\'t exist in our training set')
    else:
        word_list = start.split(' ')
        while len(word_list) < num_words:
            word_list.append(random_trigram(trigrams[word_list[-2] + ' ' + word_list[-1]]))
        return ' '.join(word_list)
