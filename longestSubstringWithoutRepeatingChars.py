def lengthOfLongestSubstringWithoutRepeatingChars(string):
  seen = {}
  start = 0
  max_length = 0
  for end, el in enumerate(string):
    if el in seen:
      start = max(start, seen[el] + 1)
    seen[el] = end
    max_length = max(max_length, end - start + 1)
  return max_length

print(lengthOfLongestSubstringWithoutRepeatingChars("abcabcbb") == 3)
#pat let's discuss
#sliding window









#https://www.youtube.com/watch?v=sZosU8JjVaA
