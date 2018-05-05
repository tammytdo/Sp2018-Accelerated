import random

def find_lightening_talk_order():
    raw_names = '''
Kouadio Assouman
Brianna Dean
Tammy Do
Ryan Drovdahl
Kristian Francisco
Jay Johnson
Andy Kwon
Mathew Martin
Wayne Olson
Aarthi Ravichander
Meet Shah
Ornob Siddiquee
Stephen Soukasene
Gokul Vasistinactive
Andrew Wall
Wesley Wang
Ruohan Zhang'''

    names = raw_names.split('\n')
    names = [name.strip() for name in names if name.strip() and 'inactive' not in name]

    random.shuffle(names)

    print(names)

find_lightening_talk_order()