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


def list_add(trigram, list):
    kata_list = []
    return kata_list.append(random_trigram(trigram[list[-2] + ' ' + list[-1]]))

def text_generator(text, start, num_words = 10):
    trigrams = dictionary_builder(text)
    if start not in trigrams:
        print('The phrase you provided doesn\'t exist in our training set')
    else:
        kata_list = start.split(' ')
        try:
            while len(kata_list) < num_words:
                addition = list_add(trigrams, kata_list)
                kata_list = addition
            return ' '.join(kata_list)
        except TypeError:
                print(kata_list)
