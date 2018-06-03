#!/usr/bin/env python

#Trigrams 
import pprint
import random

sample = "Mr. Dursley was the director Dursley was saikat of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache."
words2 = sample.split()
#print(type(words2)) #confirming that this is a list
#print(words2)

def parse_file(filename):
	with open(filename) as infile:
		#which file in file name?
		#Think of way to do this without bluntly skipping 61 lines
		for _ in range(61):
			infile.readline()
		words = []
		for line in infile:
			if line.startswith("End of the Project Gutenberg"):
				break
			wrds = line.split()
			words.extend(wrds)
	return words



def build_trigram(words):
	tris = {}
	for i in range(len(words)-2):
		first = words[i]
		second = words[i+1]
		third = words[i+2]
		#print(first,second,third)
		#tris = (first, second, third)
		pair = (first, second)	
		# followers = tris.setdefault(pair, [])
		# followers.append(third)
		if pair in tris:
			tris[pair].append(third)
		else:
			tris[pair]=[third]
	#pp = pprint.PrettyPrinter(indent = 2)
	#pp.pprint(tris)
	return tris


def make_new_text(trigram):
	pair = random.choice(list(trigram.keys()))
	sentence = []
	sentence.extend(pair)
	#Had fun playing around with the number of instances on this loop
	for i in range(100):
		if pair not in trigram:
			pair = random.choice(list(trigram.keys()))
		followers = trigram[pair]
		sentence.append(random.choice(followers))
		pair = tuple(sentence[-2:])
	return sentence

#Test with smaller file shown above
def mytestfxn():
	newtext = build_trigram(words2)
	weirdtext = make_new_text(newtext)
	nicetext =  ' '.join(weirdtext)
	print(nicetext)

if __name__ == "__main__":
	words = parse_file("sherlock.txt")
	#print(words)
	trigram = build_trigram(words)
	#This was a mistake and went on FOREVER
	#pp = pprint.PrettyPrinter(indent = 2)
	#pp.pprint(trigram)
	text = make_new_text(trigram)
	nicertext = ' '.join(text)
	print(nicertext)