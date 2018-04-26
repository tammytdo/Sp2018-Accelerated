
def fibinacci_series(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibinacci_series(n - 1) + fibinacci_series(n - 2)



print(fibinacci_series(15))

assert fibinacci_series(15) == 610

#step 2

#Test figures
# L00 = 2,  L01 = 1,  L02 = 3,  L03 = 4,  L04 = 7,   L05 =11,  L06 = 18, L07 = 29
# L08 = 47, L09 = 76, L10 = 123,L11 = 199,L12 = 322, L13 = 521 L14 = 843 L15 = 1364


def lucas_series(n):
    if n == 0:
        return (2)
    elif n == 1:
        return(1)
    return lucas_series (n-1) + lucas_series (n-2)

assert lucas_series(15) == 1364

#step 3

#Calls the defined functions above

def sum_series1 (n,lucas0=None,lucas1=None):
    if lucas0 ==2 and lucas1 == 1:
        return lucas_series(n)
    else:
        return fibinacci_series(n)

print(sum_series1(15,2,1))

# Build sum_series without lucas and fibonacci functions


# def sum_series(n, s0=None, s1=None):
#     print("called:", n)
#     if n == 0:
#         return s0
#     elif n == 1:
#         return s1
#     else:
#         return (sum_series(n - 1, s0, s1) +
#                 sum_series(n - 2, s0, s1)
#                 )

def sum_series(n, s0=None, s1=None):
    print("called:", n)
    if n == 0:
        return s0
    elif n == 1:
        return s1
    else:
        a, b = s0, s1
        for i in range(n-1):
            b, a = a + b, b
        return b


def fib(n):
    return sum_series(n, 0, 1)

def lucas(n):
    return sum_series(n, 2, 1)


# fib
assert sum_series(0, 0, 1) == 0
assert sum_series(1, 0, 1) == 1
assert sum_series(3, 0, 1) == 2

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3

# # lucas
assert  sum_series(0, 2, 1) == 2
assert  sum_series(1, 2, 1) == 1
assert sum_series(15, 2, 1) == 1364

assert lucas(15) == 1364



print("all asserts passed")

# print(sum_series(15,2,1))
