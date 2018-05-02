'''
Jay Johnson
String Formatting
////

Goal
In this exercise we will reinforce the important concepts of string formatting,
so that these start to become second nature!

Procedure
Be sure to follow all the steps described in the Procedure section of the
List Lab Exercise but this time,
create a new file called strformat_lab.py in your student dir in the class repo.
When the empty script is available and runnable, complete the following six tasks.

'''
#!/usr/bin/env python3


# Task One
#Write a format string that will take the following four element tuple:
#( 2, 123.4567, 10000, 12345.67)
#and produce:
#'file_002 :   123.46, 1.00e+04, 1.23e+04'


fnames = [2, 123.4567, 10000, 12345.67]
l = len(fnames)
#print(l)
#fnames = ['file1', 'file2', 'file10', 'file11']
#fnames.sort()
new = []
#print(fnames)
new = "{}, {}, {}, {}".format(*fnames)
#print(new)

def file_format(seq):
    file_new = seq[0]
    fnames[0] = "file_00{}".format(file_new)
    return print(fnames[0])

file_format(fnames)

def round_two_digits(seq):
    file_new = seq[1]
    fnames[1] = "{:.2f}".format(file_new)
    return print(fnames[1])

round_two_digits(fnames)

def round_two_digits_scientific(seq):
    file_new = seq[2]
    fnames[2] = "{:.2E}".format(file_new)
    file_new = seq[3]
    fnames[3] = "{:.2E}".format(file_new)
    return print(fnames[2],fnames[3])

round_two_digits_scientific(fnames)

print(fnames)
