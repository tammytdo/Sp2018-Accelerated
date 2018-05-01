'''
The following functions are exercises in sequence
manipulation.  They will take in an argument and return a
manipulated sequence.
'''


def exchangeFirstLast(seq):
    newseq = seq[-1:] + seq[1:-1] + seq[0:1]
    return newseq


def letterRemoval(seq):
    newseq = seq[0:len(seq):2]
    return newseq


def noFirstLast4(seq):
    if len(seq) > 8:
        newseq = (seq[4:-4])
        return newseq
    else:
        print(seq, " Does not have enough items to remove 8 items.")


def reversal(seq):
    newseq = seq[:: -1]
    return newseq


def mixedThirds(seq):
    units = len(seq) // 3
    newseq = seq[units:2 * units] + seq[2 * units:] + seq[0:units]
    return newseq
