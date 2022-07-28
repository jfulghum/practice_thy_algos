import collections 

# https://leetcode.com/problems/valid-sudoku/submissions/

def solution(grid):
            
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    
                
    for r in range(9):
        for c in range(9):
            if (grid[r][c] in rows[r] or grid[r][c] in cols[c] or grid[r][c] in squares[(r // 3, c // 3 )]):
                return False
            cols[c].add(grid[r][c])
            rows[r].add(grid[r][c])
            squares[(r // 3, c // 3)].add(grid[r][c])
    
    return True
