#!/usr/bin/env python3

''' trigrams '''
import string
import random

file_name = 'sherlock.txt'
with open(file_name) as f_handle:
# find the real content we need from the file
    text = []
    good_data = False
    for line in f_handle:
        good_data = good_data or (line == 'To Sherlock Holmes she is always THE woman. I have seldom heard\n')
        if good_data:
            text.append(line)
        if line == 'Walsall, where I believe that she has met with considerable success.\n':
            text.append(line)
            break
    text = ' '.join(text)
# deltet the punctuation

table = str.maketrans(dict.fromkeys(list(string.punctuation)))
text = text.strip().translate(table)

words = text.split()
datas = {}
for i in range(len(words)-3):
    key = (words[i], words[i+1])
    datas.setdefault(key,[]).append(words[i+2])



def new_text():
    print('strat the new-tet_functon')
    print(len(datas))
    for k in datas:
        break
    new = ''
    for i in range(100):
        followers = datas.get(k)
        if followers:
            new_word = random.choice(followers)
            new += ' ' + new_word
            k = (k[1], new_word)
    print(new)
    return new
