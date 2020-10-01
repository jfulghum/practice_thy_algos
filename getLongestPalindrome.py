def findLongestPalindrome(s: str, i: int, j: int) -> list:
    while i >= 0 and j < len(s):
        if s[i] != s[j]:
            break
        i -= 1
        j += 1
    return [i,j]

def longestPalindrome(s: str) -> str:
  current_longest = [0,1]
  for i in range(len(s)):
    odd = findLongestPalindrome(s, i -1, i + 1)
    even= findLongestPalindrome(s, i -1, i)
    longest = max(odd, even, key = lambda x: x[1] - x[0])
    current_longest = max(longest, current_longest, key = lambda x: x[1] - x[0])
  return s[current_longest[0]:current_longest[1]]


print(longestPalindrome(string))
