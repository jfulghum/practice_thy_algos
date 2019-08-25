def exponent(base, num):
  product = 1
  for n in range(num):
    product *= base
  return product

print(exponent(2,3))
