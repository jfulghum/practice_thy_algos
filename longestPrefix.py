input = ["flower","flow","flight"] # "fl"
input2 = ["c","acc","ccc"] # ""

def longestPrefix(input):
  if len(input) == 0: return ""
  longest_pre = input[0]
  for i in range(1, len(input)):
    while input[i].startswith(longest_pre) == False:
      longest_pre = longest_pre[:-1]
      if len(longest_pre) == 0: return ""
  return longest_pre


print(longestPrefix(input))
print(longestPrefix(input2))
