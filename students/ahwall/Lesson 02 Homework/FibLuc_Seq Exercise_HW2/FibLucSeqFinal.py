'''The program finds both the n value of a fibinacci sequence and lucas
sequence.  The last function in this program will decide which sequence is
displayed, depending on the parameters given.
'''


'''uses for loop with if else conditions to determine the fibinacci number of
a given x parameter.
'''


def fibinacci(x):
    a = 0
    b = 1
    c = 0
    if (x == 0):
        print(x)
    else:
        for i in range(x):
            a = b
            b = c
            c = b + a
        print(c)


'''uses for loop with if else conditions to determine the lucas number of
a given x parameter.
'''


def lucas(x):
    a = 2
    b = 1
    if x == 0:
        print(2)
    elif x == 1:
        print(1)
    else:
        for i in range(2, x + 1):
            c = b + a
            a = b
            b = c
        print(c)


'''uses 'if-else conditions' for the parameters being passed.  The default
function is a fibinacci return.  If a and b equal 2 and 1 respectively, then
lucas number is returned.  perameters a and b are optional, x is required.
'''


def sum_series(x, a = 0, b = 1):
    if (a == 2) and (b == 1):
        lucas(x)
    else:
        fibinacci(x)
