# https://replit.com/@jfulghum/StarryOrchidShoutcast#main.py
# https://leetcode.com/problems/remove-invalid-parentheses/


# Given a string s that contains parentheses and letters, 
# remove the minimum number of invalid parentheses 
# to make the input string valid.
# Return all the possible results. You may return the answer in any order.


class Solution:
    def removeInvalidParentheses(self, s: str):
        min_remove = 0
        start = 0
        for i in s:
            if i == "(":
                start += 1
            if i == ")":
                if start == 0:
                    min_remove += 1
                else:
                    start -= 1
        min_remove += start
        res = set() 
        def dfs(op, cl, pos, slate, min_remove):
            if pos == len(s):
                if op == cl and min_remove == 0 :
                    res.add(slate)
                return 
            if min_remove < 0:
                return          
            if s[pos] == "(":             
                dfs(op+1, cl, pos+1, slate + "(", min_remove)
                dfs(op, cl, pos+1, slate, min_remove-1)
            elif s[pos] == ")":
                if op > cl:
                    dfs(op, cl+1, pos+1, slate + ")", min_remove)
                dfs(op, cl, pos+1, slate, min_remove-1)
            else:
                dfs(op, cl, pos+1, slate + s[pos], min_remove)
        dfs(0, 0, 0, "", min_remove)          
        return res if res else [""]



print(Solution().removeInvalidParentheses("())"), ["()"])

# print(Solution().removeInvalidParentheses("()())()"), ["(())()","()()()"])
