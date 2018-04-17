def sum_series(n, input1=0, input2=1):
    if n == 0:
        return input1
    if n == 1:
        return input2

    return sum_series(n-1, input1, input2) + sum_series(n-2, input1, input2)


def fib(n):
  return sum_series(n, 0, 1)


print(fib(10))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(5))



def lucas(n):

 return sum_series(n, 2, 1)

print(lucas(0))
print(lucas(1))
print(lucas(2))
print(lucas(5))
print("Print lucas(10)")
print(lucas(10))


print("Output same value as lucas(10)")
print(sum_series(10, 2, 1))
