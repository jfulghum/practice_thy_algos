# backtrack(candidate)

# if condition
# return candidate

# if not:
  # return


# for addition in additions:
# backtrack(combine(candidate, addition))


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
