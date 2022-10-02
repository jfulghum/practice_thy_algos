# Euclid's algorithm for finding the greatest common divisor (GCD) of two numbers a and b is:
# gcd(a, 0) := a
# gcd(a, b) := gcd(b, a mod b)
# Write a function which implements Euclid's algorithm and finds the GCD of two numbers.
# For more information on this very old algorithm, check out this video. Wikipedia also has a detailed but rather formal write up.
# Function Signature

def gcd(a: int, b: int) -> int:
  if b == 0:
    return a
  return gcd(b, a % b)
 
  

  
# Expected Runtime
# O(log ab)
# Examples
print(gcd(9, 27) == 9)
print(gcd(27, 9) == 9)
print(gcd(3, 1) == 1)
print(gcd(0, 5) == 5)
