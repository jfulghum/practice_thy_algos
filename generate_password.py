# Prompt
# Given a set of characters, a minimum length, and a maximum length, generate all strings that can be created using characters from the set between the minimum and maximum lengths (inclusive).
# Function Signature

# Expected Runtime
# O(L^maxLength), where L is the length of the list

# Python 3 program to print all
# possible strings of length k
     
# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()
  


def generatePasswords(alphas, n, k):
  "".join(alphas)
  results = []
  while n <= k:
    helper(alphas, "", len(alphas), n, results)
    n += 1
  return results

def helper(alphas, prfx, l, k, results):
    if k==0:
      results.append(prfx)
    else:
      for i in range(l):
        newPrfx = prfx + alphas[i]
        helper(alphas, newPrfx, l, k-1, results)

print(generatePasswords(["a"], 2, 4) == [
  "aa",
  "aaa",
  "aaaa",
])

