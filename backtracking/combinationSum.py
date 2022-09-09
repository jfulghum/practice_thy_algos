
 
 
 class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        
        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(list(comb))
                return
            
            elif remain < 0:
                return 
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                
                backtrack(remain - candidates[i], comb, i)
                
                comb.pop()
                
        backtrack(target, [], 0)
        
        return results 
        
        
        
units= [1, 2]
target= 4
# Output:
# [[1,1,1,1], 
#  [1,1,2], 
#  [2,2]]
 
Solution().combinationSum(units, target)
        
