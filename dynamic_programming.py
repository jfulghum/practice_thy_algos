# https://leetcode.com/problems/minimum-falling-path-sum/submissions/

class Solution:
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def findMinFallingSum(matrix, row, col, memo):
            if col < 0 or col == len(matrix):
                return float('inf')
            
            if row == len(matrix) - 1:
                return matrix[row][col]
            
            if memo[row][col] != None:
                return memo[row][col]
            
            left = findMinFallingSum(matrix, row + 1, col, memo);
            middle = findMinFallingSum(matrix, row + 1, col + 1, memo);
            right = findMinFallingSum(matrix, row + 1, col - 1, memo);
            memo[row][col] = min(left, min(middle, right)) + matrix[row][col];
            return memo[row][col]
        
        minFallingSum = float('inf')
        n = len(matrix)
        memo = [[None for _ in range(n)] for _ in range(n)] 
        
        
        for startCol in range(len(matrix)):
            minFallingSum = min(minFallingSum, findMinFallingSum(matrix, 0, startCol, memo))
        
        return minFallingSum
      
# matrix = [[2,1,3],[6,5,4],[7,8,9]]

# print(minFallingPathSum(matrix)) #13
        
