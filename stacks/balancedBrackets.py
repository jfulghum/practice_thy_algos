string = "[}" # False
string1 = "[]{}"

def balancedBrackets(string):
  closed = "}])"
  opened = "{[("
  match = dict(zip(closed, opened))
  brackets = [x for x in string]
  stack = []
  for bracket in brackets:
    if bracket in opened:
      stack.append(bracket)
    else:
      if stack:
        if stack.pop() != match[bracket]: return False
      else:
        return False
  return not stack

print(balancedBrackets(string))
print(balancedBrackets(string1))
