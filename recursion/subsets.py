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
        
    
