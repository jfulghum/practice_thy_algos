from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)
        if ns < np:
            return []
        result = []
        
        s_count = Counter()
        p_count = Counter(p)
        
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            if s_count == p_count:
                result.append(i - np + 1)
        return result
