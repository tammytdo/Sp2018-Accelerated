#!/usr/bin/env python

test_string = ("My dear, here we must run as fast as we can, just to stay in place. And if you wish to go anywhere "
               "you must run twice as fast as that.")
test_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59)


def first_last_exchanged(sequence):
    return sequence[-1], sequence[1:-2], sequence[0]


def remove_every_other(sequence):
    return sequence[::2]


def first_last4removed(sequence):
    """Remove first and last 4 items and every other item in between."""
    return sequence[4:-4:2]


def reversed_(sequence):
    """Completely reverse all elements."""
    return sequence[::-1]


def thirds_rearranged(sequence):
    """Rearrange the thirds of the sequence. New order = last third, first third, middle third."""
    sect = len(sequence)//3
    return sequence[sect * 2:] + sequence[0:sect] + sequence[sect:-sect]


if __name__ == "__main__":

    print(first_last_exchanged(test_string))

    assert first_last_exchanged(test_string) == (".", "y dear, here we must run as fast as we can, just to stay in "
                                                 "place. And if you wish to go anywhere you must run twice as fast "
                                                 "as tha", "M")
    # assert first_last_exchanged(test_tuple) == (59, (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47), 2)

    print(remove_every_other(test_string))

    assert remove_every_other(test_string) == "M er eew utrna ata ecn utt tyi lc.Adi o iht oayhr o utrntiea ata ht"
    # assert remove_every_other(test_tuple) == (2, 5, 11, 17, 23, 31, 41, 47, 59)

    print(first_last4removed(test_string))

    assert first_last4removed(test_string) == "er eew utrna ata ecn utt tyi lc.Adi o iht oayhr o utrntiea ata "
    # assert first_last4removed(test_tuple) == (11, 17, 23, 31, 41)

    print(reversed_(test_string))

    assert reversed_(test_string) == (".taht sa tsaf sa eciwt nur tsum uoy erehwyna og ot hsiw uoy fi dnA ."
                                      "ecalp ni yats ot tsuj ,nac ew sa tsaf sa nur tsum ew ereh ,raed yM")
    # assert reversed_(test_tuple) == (59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2)

    print(thirds_rearranged(test_string))

    assert thirds_rearranged(test_string) == ("o anywhere you must run twice as fast as that."
                                              "My dear, here we must run as fast as we can,"
                                              " just to stay in place. And if you wish to go ")
    # # assert thirds_rearranged(test_tuple) == ((31, 37, 41, 43, 47, 53, 59),
    #                                          (2, 3, 5, 7, 11),
    #                                          (13, 17, 19, 23, 29, 31, 37))
