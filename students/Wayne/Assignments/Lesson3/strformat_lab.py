# String Formatting Lab Exercise

# References

# https://canvas.uw.edu/courses/1197533/assignments/4129960?module_item_id=8240359
# https://docs.python.org/3/library/string.html#format-string-syntax
# https://pyformat.info/
# https://mkaz.tech/python-string-format.html

# Procedure
# Be sure to follow all the steps described in the Procedure section of the
# List LabExercise but this time, create a new file called strformat_lab.py
# in your student dir in the class repo.

# When the empty script is available and runnable, complete the following
# six tasks.

# Task One

# Write a format string that will take the following four element tuple:

# (2, 123.4567, 10000, 12345.67))


"""

String presentation types:

d = decimal integer and ouputs the number in base 10
f = shows how many figures should be displayed after the
    decimal point
g = shows the before and after the decimal point
e = prints the number in scientific noation using
    letter e to indicate the exponent. Defualt
    precision is 6.

    https://docs.python.org/3.4/library/string.html

"""

print("File_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))
print()

# Task Two

# Using your results from Task One, repeat the exercise, but this time using an
# alternate type of format string (hint: think about alternative ways to use
# .format() (keywords anyone?), and also consider f-strings if you’ve not used
# them already).

# Task Three

# Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1, 2, 3)

# def formatter(in_tuple):
#    do_something_here_to_make_a_format_string
#
#    return form_string.format(in_tuple)

jennyfromdablock = (8, 6, 7, 5, 3, 0, 9)


def format_string(i):
    formattedstring = 'The {:d} numbers are '.format(len(i))
    print(formattedstring)
    formattedstring += ','.join(['{:d}'] * len(i))
    print(formattedstring)
    return formattedstring.format(*i)
    print(formattedstring)


# Task Four

# Given a 5 element tuple:

# ( 4, 30, 2017, 2, 27)

# use string formating to print:

# '02 27 2017 04 30'

# Hint: use index numbers to specify positions.

a_tuple = (4, 30, 2017, 2, 27)

new_atuple = a_tuple[3:5] + a_tuple[2:3] + a_tuple[0:2]

print(new_atuple)

# Task Five

# f-strings are new to Python (version 3.6), but are very powerful and
# efficient. This fruit in means they are worth understanding and using.
#  And this is made easier than it might be because they use the same,
# familiar formatting language that is conventionally used in Python
# (in .format()).

# Here’s a task for you: Given the following four element list:

# ['oranges', 1.3, 'lemons', 1.1]

# Write an f-string that will display:

# The weight of an orange is 1.3 and the weight of a lemon is 1.1

# Now see if you can change the f-string so that it displays the names of
# the  fruit in upper case, and the weight 20% higher (that is 1.2 times
# higher).









# Task Six

# Write some Python code to print a table of several rows, each with a name,
#  an age and a cost. Make sure some of the costs are in the hundreds and
# thousands to test your alignment specifiers.

# And for an extra task, given a tuple with 10 consecutive numbers, can
# you work how to quickly print the tuple in columns that are 5 charaters
# wide? It’s easily done on one short line!
