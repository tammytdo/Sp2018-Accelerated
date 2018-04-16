
def fib(n):

  if n == 0:
    return 0
  return n + fib(n-1)


print(fib(10))
print(fib(1))
print(fib(2))
