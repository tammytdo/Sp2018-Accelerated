
def fib(n):

  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-1) + fib(n-2)


print(fib(10))
print(fib(1))
print(fib(2))
print(fib(3))



def lucas(n):

  if n == 0:
    return 2
  if n == 1: 
    return 1

  return lucas(n-1) + lucas(n-2)


print(lucas(0))
print(lucas(1))
print(lucas(2))
print(lucas(5))

