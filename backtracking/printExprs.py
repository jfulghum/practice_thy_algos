'''
Given a string that contains only digits from 0 to 9, and an integer value, target. Print all expressions which evaluate to target using the plus(+) and minus(-) binary operators between the digits.
'''

"""
"12" # 2

operations = [+, -, *, /]
result = []

def helper(num, operation, expression):
   if len(nums in expression) == len(seq):
        evaluate expression
        # eval
        if expression == target:
            result.append(expression)
            return 
        return

    return



interate over seq 

    check if:


    for operation in operations:
        if not last num:
            expression = num + operation
        else:
            expression = num
        helper(num, operation, expression)

""" 

"12"

def printExprs(seq: str, target: int) -> None:

    def helper(expression, operation):
        if num != seq[-1]:
            expression += num + operation
        else:
            expression += num

        if len(expression) == len(seq) * 2 - 1:
            evaluation = eval(expression)
            if evaluation == target:
                print(expression)
                return 
            return
        return

   
    expression = ''
    for num in seq:
        helper(expression, "-")
        helper(expression, "+")

printExprs(seq="12", target=2)
#1*2

# + 
# 2 + 0 + 1

# 2 - 0 - 1

   2
  + -
 0.   0 
+ -   + - 
1 1.  1. 1




# 201, 3
# 2 + 0 + 1
# 2 - 0 + 1
printExprs(seq="201", target=3)

# 201, 19
# 20 - 1 

'''
printExprs(seq="123", target=6); print("====") # plus only
# 1+2+3

printExprs(seq="125", target=7); print("====") # minus only
# 12-5

printExprs(seq="1236", target=0); print("====") # mix
# 1+2+3-6

printExprs(seq="1235", target=-3); print("====") # mix
# 1-2+3-5

printExprs(seq="12036", target=0); print("====")
# 1+2+0+3-6
# 1+2-0+3-6

printExprs(seq="12036", target=18); print("====")
# 1+20+3-6

printExprs(seq="1010", target=9); print("====")
# 10-1+0
# 10-1-0

printExprs(seq="420", target=420); print("====")
# 420

printExprs(seq="1210", target=2); print("====")
# 1+2-1+0
# 1+2-1-0
# 12-10
'''
