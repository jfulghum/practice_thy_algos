# backtrack(candidate)

# if condition
# return candidate

# if not:
  # return


# for addition in additions:
# backtrack(combine(candidate, addition))


# this is dfs not backtracking

def backtrack(K, str, n):

  if n == K:
    print("".join(str), sep = "", end = " ")
    return 

  if str[n-1] == "0":
    str[n] = "0"
    backtrack(K, str, n+1)
    str[n] = "1"
    backtrack(K, str, n+1)

  if str[n - 1] == "1":
    str[n] = "0"
    backtrack(K, str, n+1)

  

def printBinaryWithoutConsecutive1s(K: int) -> None:

  if K <= 0:
    return

  str = [0] * K 

  str[0] = "0"
  backtrack(K, str, 1)

  str[0] = "1"
  backtrack(K, str, 1)


printBinaryWithoutConsecutive1s(3)

# 000 001 010 100 101 



'''
Problem

Given an integer maxLen, print all binary strings of size maxLen that don't have 1s next to each other. That is, no string should contain the substring 11, 111, 1111, 11111, etc. You can assume maxLen > 0.
Function Signature: 
def printBinaryWithoutConsecutive1s(maxLen: int) -> None:
Target runtime and space complexity:
Time: O(2^n) where n is the length of the binary string. There are n indexes and each index can be either 0 or 1 with some small exceptions
Space: O(n) because the stack can reach n recursive frames before being torn down
Examples:



printBinaryWithoutConsecutive1s(maxLen=1)
0
1

printBinaryWithoutConsecutive1s(maxLen=2)
00
01
10

printBinaryWithoutConsecutive1s(maxLen=3)
000
001
010
100
101
'''


'''
state = 001
maxLen=3
                    ()
              0             1     
        0          1
    0       1
'''


# backtrack

# if condition
#  return x

# if not condition:
#     return

# for possibilty in possiblities


# def dfs(k, str, i):

#     if i == maxLen:
#     print str

#     see if previous i is 1 and if so,
#     if str[i-1] == "1":
#     str[i] = 0
#     dfs(k, str, i + 1) 

#     see if previous i is 0 and if so,
#     str[i] = 0
#     dfs(k, str, i + 1) 


#     str[i] = 1
#     dfs(k, str, i + 1) 

def dfs(maxLen, string, i):

    if i == maxLen:
        print("".join(string))
        print()
        return

    if i == 0:
        string[i] = "0"
        dfs(maxLen, string, i + 1)

        string[i] = "1"
        dfs(maxLen, string, i + 1)

    elif string[i-1] == "1":
        string[i] = "0"
        dfs(maxLen, string, i + 1)

    elif string[i-1] == "0":
        string[i] = "0"
        dfs(maxLen, string, i + 1)

        string[i] = "1"
        dfs(maxLen, string, i + 1)


def printBinaryWithoutConsecutive1s(maxLen):
    if maxLen <= 0:
        return None

    string = ["0"] * maxLen # ["0",0",0] "".join(["0", "1", "0"])

    dfs(maxLen, string, 0)


printBinaryWithoutConsecutive1s(3)
# printBinaryWithoutConsecutive1s(2)
