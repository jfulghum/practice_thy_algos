# Ternary is a base-3 number system that uses the digits 0, 1, and 2, similar to how decimal uses 0-9 and binary uses 0 and 1.
# Given an integer, write a function that converts the number into its base 3 representation. Return the result as a string.
# Function Signature:

# symbols = 0, 1, 2
# 9  -> 100
# 16 -> 121 
# 16 % 3 = 1
# 16 - 1 = 15 / 3 = 5

# 5 % 3 = 2
# 5 - 2 = 3 / 3 = 1

# 1 % 3 = 1
# 1 - 1 = 0 / 3 = 0

def convertToBase3(n: int) -> str:
    if n == 0:
        return 0

    ternarySymbols = ['0', '1', '2']
    isNegative = n < 0
    result = ''

    if isNegative:
        n *= -1

    while n > 0:
        result = ternarySymbols[int(n % 3)] + result
        n = (n - (n % 3)) / 3

    if isNegative:
        return int(result) * -1

    return int(result)
#
print(convertToBase3(9))  #  100
print(convertToBase3(-9)) # -100
print(convertToBase3(0)) # 0
print(convertToBase3(16)) # 121 
