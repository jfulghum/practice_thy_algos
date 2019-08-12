input = ["flower","flow","flight"]


def longestPrefix(input):
  longest_pre = input[0]
  for i in range(1, len(input)):
    while input[i].find(longest_pre) == -1:
      longest_pre = longest_pre[:-1]
      if len(longest_pre) == 0: return 0
  return longest_pre




print(longestPrefix(input))
