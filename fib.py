
#print the nth fib number
def fib(n):
  if n <= 2: return n
  a = b = 1
  for i in range(2,n):
    a, b = b, a+b
  return b


print(fib(6))
# 1,1,2,3,5,8

