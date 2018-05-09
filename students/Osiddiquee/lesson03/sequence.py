def exchange_first_last(seq):
    return seq[-1] + seq[1 : len(seq) - 1] + seq[0]

def remove_every_other(seq):
    return seq[:: 2]

def remove_first_lastfour(seq):
    return seq[1: len(seq) - 4]

def reversed(seq):
    return seq[::-1]

def third_shuffle(seq):
    return (seq[len(seq)//3 : 2 * len(seq)//3] +
            seq[2 * len(seq)//3 :] +
            seq[: len(seq)//3]
            )

#assertions for exchange_first_last(seq)
assert exchange_first_last('X this is a test Y') == 'Y this is a test X'

#assertions for remove_every_other(seq)
assert remove_every_other('XYXYXYXYXYXYX') == 'XXXXXXX'
assert remove_every_other('XYXYXYXYXYXYXO') == 'XXXXXXX'

#assertions for remove_first_lastfour(seq)
assert remove_first_lastfour('YAAAXXXX') == 'AAA'

#assertions for reversed(seq)
assert reversed('ABCD') == 'DCBA'

#assertions for third_shuffle(seq)
assert third_shuffle('XXXYYYZZZ') == 'YYYZZZXXX'

print('All asserts passed!')
