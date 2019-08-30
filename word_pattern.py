string = "jo han jo han"
pattern = "abab"

def word_pattern(string, pattern):
  words = string.split(" ")
  if len(words) != len(pattern):
    return False
  return [pattern.find(x) for x in pattern] == [words.index(x) for x in words]
  # return list(map(pattern.find, pattern)) == list(map(words.index, words))

print(word_pattern(string, pattern))


# This is the extension problem of Word Pattern I.
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# def word_pattern_II(string,pattern):


# print(word_pattern_II("abab", "redblueredblue" == True)
# print(word_pattern_II("aaaa", "asdasdasdasd" == True)
# print(word_pattern_II("aabb", "xyzabcxzyabc" == False)

# class Solution(object):
#     '''算法思路：
#     同 I，只是用了 tracebacking，有点疑惑的是，OJ 上不能写成这样的形式：
#         def wordPatternMatch(self, pattern, str, {}, {}):
#     '''
#     def match(self, pattern, str, r1, r2):
#         if not (pattern or str):
#             return True

#         if not pattern and str or pattern and not str:
#             return False

#         char = pattern[0]
#         for j in xrange(len(str)):
#             substr = str[:j + 1]
#             if char not in r1 and substr not in r2:
#                 r1[char] = substr
#                 r2[substr] = char

#                 if self.match(pattern[1:], str[j + 1:], r1, r2):
#                     return True

#                 del r1[char]
#                 del r2[substr]

#             elif (char in r1 and r1[char] == substr and
#                     self.match(pattern[1:], str[j + 1:], r1, r2)):
#                 return True

#         return False

#     def wordPatternMatch(self, pattern, str):
#         r1, r2 = {}, {}
#         return self.match(pattern, str, r1, r2)


# s = Solution()
# print s.wordPatternMatch('aabb', 'xyzabcxzyabc')
