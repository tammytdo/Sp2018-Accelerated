# Work on the Python exercises at “Coding Bat”: http://codingbat.com/python
#
# Warmup-1 > sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True
def sleep_in(weekday, vacation):
    if weekday == vacation:
        return True
    elif weekday is True and vacation is False:
        return False
    elif weekday is False and vacation is True:
        return True
    return

# Warmup-1 > monkey_trouble

# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
    return
