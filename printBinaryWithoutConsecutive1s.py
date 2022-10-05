def printBinaryWithoutConsecutive1s(maxLen: int) -> None:

  def helper(temp):
    
    if len(temp) == maxLen:
      print(temp)
      return
      
    if temp[-1] == "1":
      helper(temp + "0")
    else:
      helper(temp + "0")
      helper(temp + "1")
      

  helper("0")
  helper("1")
  

  
# Target runtime and space complexity:
# Time: O(2^n) where n is the length of the binary string. There are n indexes and each index can be either 0 or 1 with some small exceptions
# Space: O(n) because the stack can reach n recursive frames before being torn down
# Examples:
printBinaryWithoutConsecutive1s(maxLen=2)
# 00
# 01
# 10

printBinaryWithoutConsecutive1s(maxLen=3)
# 000
# 001
# 010
# 100
# 101
