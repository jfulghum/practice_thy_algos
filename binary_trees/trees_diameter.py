def solution(t):
    result = [0]
    def findMaxPath(t):
        if t is None:
            return 0
        left = findMaxPath(t.left)
        right = findMaxPath(t.right)
        temp = max(left, right) + 1
        result[0] = max(result[0], left + right + 1)
        return temp
    findMaxPath(t)
    return result[0]
    
