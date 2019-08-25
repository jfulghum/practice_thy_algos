
#print the nth fib number
def fib(n):
  if n <= 2: return n
  a = b = 1
  for i in range(2,n):
    a, b = b, a+b
  return b


print(fib(6))
# 1,1,2,3,5,8


def fib_recursive(n):
  if n <= 2: return 1
  return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(4))

def fib_cache(n, cache = {1:1, 2:1}):
  if n in cache: return cache[n]
  cache[n] = fib_cache((n - 1),cache) + fib_cache((n-2),cache)
  return cache[n]

print(fib_cache(7))
