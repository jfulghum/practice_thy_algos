from collections import defaultdict


class Solution:
    def minTransfers(self, transactions) -> int:
        '''
        e.g. debt = [10, -5, -5] then we need to using the debt[start] (start from first non-zero element) to settle the rest
        run a dfs to possible descendants : [10, -5, -5] -> [0, 5, -5] -> [0, 0, 0]
                                              [10, -5, -5] -> [0, -5, 5] -> [0, 0, 0]
        '''
        ledger = defaultdict(int)
        for lender, receiver, amount in transactions:
            ledger[lender] -= amount
            ledger[receiver] += amount
            
        debt = [v for v in ledger.values() if v!= 0]
        if not debt:
            return 0
        
        count = float('inf')
        n = len(debt)
        def dfs(start, currCount):
            while start < n and debt[start] == 0: # cannot use debt[start] to settle if it is zero
                start += 1
        
            if start >= n - 1 :
                nonlocal count
                count = min(count, currCount)
                return 
        
            for i in range(start+1, n):
                if debt[start] * debt[i] < 0: # there is a need to settle
                    debt[i] += debt[start]
                    dfs(start + 1, currCount + 1)
                    debt[i] -= debt[start]
                    if debt[start] + debt[i] == 0: # if they happened to be complement then it is the optimal so break the loop
                        break
        dfs(0, 0)
        
        return count


# You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.
transactions = [[0,1,10],[2,0,5]]

print(Solution().minTransfers(transactions))
