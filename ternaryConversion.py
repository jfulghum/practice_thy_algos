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


"""
Ternary is a base-3 number system that uses the digits 0, 1, and 2, similar to how decimal uses 0-9 and binary uses 0 and 1.
Given an integer, write a function that converts the number into its base 3 representation. Return the result as a string.

Function Signature: 
    def convertToBase3(n: int) -> str

Target runtime and space complexity:
    O(log n)

Examples:
    convertToBase3(0) == "0"
    convertToBase3(1) == "1"
    convertToBase3(2) == "2"
    convertToBase3(3) == "10"
    convertToBase3(4) == "11"
                          
    convertToBase3(92) == "10102"
                              ^
    convertToBase3(-5) == "-12"

input 92
output 10102   

base_array = ['0', '1', '2'] 


iteration 1:
    92 % 3 = 2 

    result = "2"

    n = ( 92 - 2 )/ 3 = 30
    n = (n - (n % 3)) / 3 = 30 

iteration 2:
    30 % 3 = 0 

    result = "0" + result 
    n = ( 30 - 0 )/ 3 = 10 

iteration 3:
    10 % 3 = 1

    result = "1" + result 
    n = ( 10 - 1 )/ 3 = 3

iteration 4:
    3 % 3 = 0 

    result = "0" + result 
    n = ( 3 - 0 )/ 3 = 1

iteration 5:
    1 % 3 = 1


"""

def convertToBase3(n: int):
    if n == 0:
        return 0

    is_negative = False
    if n < 0: 
        n = abs(n)
        is_negative = True
        
    result = ''
    while n > 0:
        print(f"iteration: {i}")
        remainder = n % 2 
        result = str(remainder) + result 

        n = (n - (n % 2)) // 2

    if is_negative:
        return "-" + result

    return result



print(convertToBase3(0)) # "0"
print( convertToBase3(1)) # "1"
print( convertToBase3(2)) # "2"
print( convertToBase3(3)) # "10"
print( convertToBase3(4))  # "11"
print(convertToBase3(92)) # 10102
print(convertToBase3(-5)) # -12

print(convertToBase3(21512)) # 10102
print(math.log(21512))
