def generateNDigitTernaries(n):
  output = []
  stack = []

  def helper():
    if len(stack) == n:
      output.append("".join(stack))
      return;
    
    for i in range(3):
      stack.append(str(i))
      helper()
      stack.pop()

  for i in range(3):
    stack.append(str(i))
    helper()
    stack.pop()

  return output

print(generateNDigitTernaries(3))

# ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111', '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222']
#  
