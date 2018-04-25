#! /usr/local/bin/python3


'''
Trigrams Project

This version of the code produces a haiku of 5-7-5.  Stole the function from
'sylco' code on GitHub to return number of syllables per word

'''
import random
import re


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


def make_new_text3(trigram):
    # start the new text with any random word
    # if the random key does not start with a capital letter, then get another
    # different random key
    #
    # establish the end of sentence character
    e = ('.', '?', '!')
    pair = random.choice(list(trigram.keys()))
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

def sylco(word) :
    '''
    function derived from 'sylco' code on GitHub
    '''
    word = word.lower()
    # exception_add are words that need extra syllables
    # exception_del are words that need less syllables
    exception_add = ['serious', 'crucial']
    exception_del = ['fortunately', 'unfortunately']
    co_one = ['cool', 'coach', 'coat', 'coal', 'count', 'coin', 'coarse',
              'coup', 'coif', 'cook', 'coign', 'coiffe', 'coof', 'court']
    co_two = ['coapt', 'coed', 'coinci']
    pre_one = ['preach']
    # added syllable number
    syls = 0
    # discarded syllable number
    disc = 0
    # 1) if letters < 3 : return 1
    if len(word) <= 3:
        syls = 1
        return syls
    # 2) if doesn't end with "ted" or "tes" or "ses" or "ied" or "ies",
    # discard "es" and "ed" at the end.
    # if it has only 1 vowel or 1 set of consecutive vowels, discard. (like
    # "speed", "fled" etc.)
    if word[-2:] == "es" or word[-2:] == "ed":
        doubleAndtripple_1 = len(re.findall(r'[eaoui][eaoui]', word))
        if doubleAndtripple_1 > 1 or len(re.findall(r'[eaoui][^eaoui]', word)) > 1:
            if word[-3:] == "ted" or word[-3:] == "tes" or word[-3:] == "ses" or word[-3:] == "ied" or word[-3:] == "ies":
                pass
            else:
                disc += 1
    # 3) discard trailing "e", except where ending is "le"
    le_except = ['whole', 'mobile', 'pole', 'male', 'female', 'hale', 'pale',
                 'tale', 'sale', 'aisle', 'whale', 'while']
    if word[-1:] == "e":
        if word[-2:] == "le" and word not in le_except:
            pass
        else:
            disc += 1
    # 4) check if consecutive vowels exists, triplets or pairs, count them as
    # one.
    doubleAndtripple = len(re.findall(r'[eaoui][eaoui]', word))
    tripple = len(re.findall(r'[eaoui][eaoui][eaoui]', word))
    disc += doubleAndtripple + tripple
    # 5) count remaining vowels in word.
    numVowels = len(re.findall(r'[eaoui]', word))
    # 6) add one if starts with "mc"
    if word[:2] == "mc":
        syls += 1
    # 7) add one if ends with "y" but is not surrouned by vowel
    if word[-1:] == "y" and word[-2] not in "aeoui":
        syls += 1
    # 8) add one if "y" is surrounded by non-vowels and is not in the last word
    for i, j in enumerate(word):
        if j == "y":
            if (i != 0) and (i != len(word)-1):
                if word[i-1] not in "aeoui" and word[i+1] not in "aeoui":
                    syls += 1
    # 9) if starts with "tri-" or "bi-" and is followed by a vowel, add one.
    if word[:3] == "tri" and word[3] in "aeoui":
        syls += 1
    if word[:2] == "bi" and word[2] in "aeoui":
        syls += 1
    # 10) if ends with "-ian", should be counted as two syllables, except
    # for "-tian" and "-cian"
    if word[-3:] == "ian":
        # and (word[-4:] != "cian" or word[-4:] != "tian") :
        if word[-4:] == "cian" or word[-4:] == "tian":
            pass
        else:
            syls += 1
    # 11) if starts with "co-" and is followed by a vowel, check if exists in
    # the double syllable dictionary, if not, check if in single dictionary and
    # act accordingly.

    if word[:2] == "co" and word[2] in 'eaoui':
        if word[:4] in co_two or word[:5] in co_two or word[:6] in co_two:
            syls += 1
        elif word[:4] in co_one or word[:5] in co_one or word[:6] in co_one:
            pass
        else:
            syls += 1
    # 12) if starts with "pre-" and is followed by a vowel, check if exists in
    # the double syllable dictionary, if not, check if in single dictionary and
    # act accordingly.
    if word[:3] == "pre" and word[3] in 'eaoui':
        if word[:6] in pre_one:
            pass
        else:
            syls += 1
    # 13) check for "-n't" and cross match with dictionary to add syllable.
    negative = ["doesn't", "isn't", "shouldn't", "couldn't", "wouldn't"]
    if word[-3:] == "n't":
        if word in negative:
            syls += 1
        else:
            pass
    # 14) Handling the exceptional words.
    if word in exception_del:
        disc += 1
    if word in exception_add:
        syls += 1
    # calculate the output
    return numVowels - disc + syls


def haiku():
    # 5 syllables
    syllable_count = 0
    while syllable_count < 5:
        text = make_new_text2(trigram)
        for word in text:
            syllable_count += sylco(word.strip())
            if syllable_count < 5:
                print(word.strip('"\'.'), end=' ')
            elif syllable_count == 5:
                print(word.strip('"\'.'), end=' ')
                print('\n  ')
                break
            elif syllable_count > 5:
                syllable_count -= sylco(word.strip())
                pass
    # 7 syllables
    syllable_count = 0
    while syllable_count < 7:
        text = make_new_text3(trigram)
        for word in text:
            syllable_count += sylco(word.strip())
            if syllable_count < 7:
                print(word.strip('"\'.'), end=' ')
            elif syllable_count == 7:
                print(word.strip('"\'.'), end=' ')
                print('\n  ')
                break
            elif syllable_count > 7:
                syllable_count -= sylco(word.strip())
                pass
    # 5 syllables
    syllable_count = 0
    while syllable_count < 5:
        text = make_new_text3(trigram)
        for word in text:
            syllable_count += sylco(word.strip())
            if syllable_count < 5:
                print(word.strip('"\'.'), end=' ')
            elif syllable_count == 5:
                print(word.strip('"\'.'), end=' ')
                print('\n  ')
                break
            elif syllable_count > 5:
                syllable_count -= sylco(word.strip())
                pass
    return


if __name__ == "__main__":
    words = parse_file("sherlock.txt")
    trigram = build_trigram(words)
    text = make_new_text2(trigram)
    # print haiku
    print('Here\'s a haiku...    just for you....\n\n')
    haiku()
