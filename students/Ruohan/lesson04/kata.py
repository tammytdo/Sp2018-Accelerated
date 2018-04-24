#!/usr/bin/env python3

''' trigrams '''
import string
import random

file_name = 'sherlock.txt'
with open (file_name) as f_handle:
# find the real content we need from the file
    line_useful = ''
    bool_flag = False
    while True:
        line = f_handle.readline()
        bool_flag = bool_flag or (line == 'To Sherlock Holmes she is always THE woman. I have seldom heard\n')
        if bool_flag:
            line_useful += line
        if line == 'Walsall, where I believe that she has met with considerable success.\n':
            break

# deltet the punctuation

table = str.maketrans(dict.fromkeys(list(string.punctuation)))
line_useful = line_useful.strip().translate(table)

words = line_useful.split()
datas = {}
for i in range(len(words)-2):
    key = (words[i], words[i+1])
    datas.setdefault(key,[]).append(words[i+2])

def new_text():
    k1 = input('Enter the first word>>')
    k2 = input('Enter the second word>>')
    k = (k1,k2)
    new = ''
    while True:
        if k in datas:
            new_word = str(random.choice(datas.get(k)))
            new += ' ' + new_word
            k = (k[1],new_word)
        else:
            break
    return new
