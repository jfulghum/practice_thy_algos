# https://replit.com/@jfulghum/OvercookedAltruisticQuadrants#main.py

def valid_parathensis(n):

  def backtrack(s, left, right):
    if len(s) == n:
      ans.append("".join(s))
      return

    if left < n:
      s.append("(")
      backtrack(s, left + 1, right)
      s.pop()

    if right < left:
      s.append(")")
      backtrack(s, left, right + 1)
      s.pop()
  

  ans = []
  backtrack([], 0, 0)
  return ans


print(valid_parathensis(4))
