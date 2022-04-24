# gcd(a, 0) := a
# gcd(a, b) := gcd(b, a mod b)
# Write a function which implements Euclid's algorithm and finds the GCD of two numbers. 
# Function Signature
def gcd(x: int, y: int) -> int:
  while(y):
       x, y = y, x % y
  return x


  
# Expected Runtime
# O(log ab)
# Examples
print(gcd(9, 27) == 9)
print(gcd(27, 9) == 9)
print(gcd(3, 1) == 1)
print(gcd(0, 5) == 5)
print(gcd(9, 27) == 9)
print(gcd(27, 9) == 9)
print(gcd(3, 1) == 1)
print(gcd(0, 5) == 5)
