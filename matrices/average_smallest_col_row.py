# First, write a function that returns the average of the smallest values in each column.
# Write a new version of this function that returns the average of the smallest value in each row.

input = [
  [32, 23, 3],
  [23,  7, 5],
]

def averageColumnMinimum(input):
  values = []

  for c in range(len(input[0])):
    smallest = float('inf')
    for r in range(len(input)):
      if input[r][c] < smallest:
        smallest = input[r][c]

    values.append(smallest)
    smallest = float('inf')
    

  return sum(values) / len(values)
      
print(averageColumnMinimum(input))      

  # -> 11 (average of 23, 7, 3)
  
def averageRowMinimum(input):
  values = []

  for r in range(len(input)):
    smallest = float('inf')
    for c in range(len(input[0])):
      if input[r][c] < smallest:
        smallest = input[r][c]

    values.append(smallest)
    smallest = float('inf')
    
  return sum(values) / len(values)

print(averageRowMinimum(input))
  # -> 4 (average of 5 and 3)
