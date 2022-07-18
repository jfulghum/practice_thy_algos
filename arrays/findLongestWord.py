# Note: you must sort by length AND lexicographical order.
# meaning: dictionary.sort(key = lambda x: (-len(x), x))


# 524. Longest Word in Dictionary through Deleting
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

# Given a string s and a string array dictionary, return the longest string in the dictionary 
# that can be formed by deleting some of the given string characters. 
# If there is more than one possible result, return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.

 

# Example 1:

# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# Example 2:

# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        # sort the dictionary , firstly by length in decreasing order, 
        # if length is equal, sort by lexicographical order，
        # time complexity for this: O(dlog(d)), d is the len of dict
        dictionary.sort(key = lambda x: (-len(x), x))
        # 2 pointers, one for s, one for word
        # time complexity: O(s*c*d), s is len(s), c is the len of largerst word in dict,
        for word in dictionary:
            i = 0
            for char in s:
                if i<len(word) and word[i]==char:
                    i+=1
            # after checking each char in s and try to match it to word
            # if every char in word appears in s in its word order, then we can delete the char in s to get this word
            # since we have sorted dictionary, this word would be the best so far, so we return it directly
            if i == len(word):
                return word
            
        # no solution 
        return ""
