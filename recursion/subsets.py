# https://leetcode.com/problems/subsets/

class Solution:
    def helper(self, current, remaining, result):   
        for i in range(len(remaining)):
            new_current = current + [remaining[i]]
            result.append(new_current)
            self.helper(new_current, remaining[i+1:], result)
            
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.helper([], nums, result)
        return result
        
    

    
    
# https://neetcode.io/practice

#     another way!

# input: [1,2,3]
# [1,2]
# res: [[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3],[]]
array = [1,2,3]

#arrays are passed by reference, so anytime we change the array, it will mess up all the future

def subsets(array):
  result = []
  
  def helper(index, part):
    partCpy = part.copy()
    
    if index >= len(array):
      result.append(partCpy)
      return 
      
    # choose
    partCpy.append(array[index])
    helper(index + 1, partCpy)
  
    # don't choose
    partCpy.pop()
    helper(index + 1, partCpy)
  
  helper(0, [])
  return result
  

print(subsets(array))
