
"""
trigrams:

solutions to the trigrams project

"""
sample = """I was seized with a keen desire to see Holmes
again and to know how he was to see employing his extraordinary powers
His rooms were to know brilliantly lit"""

words = sample.split()

print(words)

def parse_file(filename):
    """
    parse text file to makelist of words
    """
    with open(filename) as infile:
        words = [ 
        for line in infile:
            print(line)
            wrds = line.split().split()
            print(wrds)
            words.extend(wrds)
            
        return words



def build_trigrams(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        print(first, second, third)
        pair = (first, second)
        list_of_followers = tris.setdefault(pair, [])
        list_of_followers.append(third)
    print(tris)
    return tris


if __name__ == "__main__":
    words = parse_file("")
    #trigram = build_trigrams(words)
