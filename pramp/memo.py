

"""
If i,j > 0 and str1[i] ≠ str2[j] then opt(i,j) = 1 + min(opt(i-1, j), opt(i, j-1))

This holds since we need to delete at least one of the letters str1[i] or str2[j]
and the deletion of one of the letters is counted as 1 deletion (hence the 1 in the formula).
Then, since we’re left with either the (i-1)'th prefix of str1, or the (j-1)'th prefix of str2,
need to take the minimum between opt(i-1,j) and opt(i,j-1).
We, therefore, get the equation opt(i,j) = 1 + min(opt(i-1,j), opt(i,j-1)).

If i,j > 0 and str1[i] = str2[j], then opt(i,j) = opt(i-1, j-1)

This holds since we don’t need to delete the last letters in order to get the same string,
we simply use the same deletions we would to the (i-1)'th and (j-1)'th prefixes."""
#heat , hit
def deletion_distance(str1, str2):


  if (len(str1) < len(str2)):
        tmpStr = str1
        str1 = str2
        str2 = tmpStr
  n1 = len(str1)
  n2 = len(str2)
  prevMemo = [0  for j in range(n2 + 1)]
  currMemo = [0  for j in range(n2 + 1)]
  for i in range(0, n1 + 1):
      for j in range(0, n2 + 1):

        if i == 0:
           currMemo[j] = j

        elif j == 0:
           currMemo[j] = i

        elif (str1[i-1] == str2[j-1]):
          print(str1[i- 1],str2[j -1])
          print("same", currMemo, prevMemo)
          currMemo[j] = prevMemo[j-1]
        else:
          print(str1[i- 1],str2[j -1])
          print("dif", currMemo, prevMemo)
          print("min", currMemo[j-1], prevMemo[j], )
          currMemo[j] = 1 + min(prevMemo[j], currMemo[j-1])
          print("Curr", currMemo)
      print(currMemo, prevMemo)
      prevMemo = currMemo
      currMemo = [0 for j in range(n2 + 1)]
      print(currMemo, prevMemo)
  return prevMemo[n2]

print(deletion_distance("hi" , "h"))
