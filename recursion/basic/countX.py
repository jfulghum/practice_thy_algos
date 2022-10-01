# Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
# Function Signature


def countX(word: str) -> int:
  if len(word) <= 0:
    return 0
    
  return int(word[0] == "x") + countX(word[1:])
  
# Expected Runtime
# Time: O(L) where L is the length of the string
# Space: O(L) where L is the length of the string when using an index or O(L^2) when slicing new strings
# Examples
print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hi") == 0)
print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hiX") == 0)
print(countX("XXXhXXX") == 0)
print(countX("x") == 1)
print(countX("") == 0)
print(countX("hihi") == 0)
print(countX("hiAAhi12hi") == 0)
