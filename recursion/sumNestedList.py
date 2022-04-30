def sumNestedList(nestedList):
    sum = 0
    for element in nestedList:
        if type(element) == int:
            sum += element
        else:
            sum += sumNestedList(element)
    return sum




print(sumNestedList(
  [1, 2, 3]
) == 6)
print(sumNestedList(
  [1, [1, 2, 3], 3]
) == 10)
print(sumNestedList(
  [1, [1, [1, [1, [1]]]]]
) == 5)
