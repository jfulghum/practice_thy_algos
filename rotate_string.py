class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(0, len(s)):
             if s[i:] + s[:i] == goal:
                return True
        return False
