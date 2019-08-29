def smallest_substring(arr, string):
  chars = set(arr)
  current = {}
  smallest = ""
  for i, char in enumerate(string):
    if char in chars:
      current[char] = i
    if len(current) == len(chars):
      temp = string[current[min(current, key = current.get)]:current[max(current, key = current.get)]+1]
      if len(temp) < len(smallest) or len(smallest) == 0:
        smallest = temp
  return smallest

arr = ['x','y','z']
string = "xyyzyzyx" # zyx

print(smallest_substring(arr, string))
