# Print all plus & minus expressions that evaluate to a target



def printExprs(seq: str, target: int) -> None:
  def calcuateExpr(curExpr: str, seq: str, target: int, curIdx: int, total: int) -> None:
    # Base case is at the end index of the sequence and the total matches target
    if curIdx == len(seq) and total == target:
      print("".join(curExpr))
      return

    # loop to put operator at all positions
    for i in range(curIdx, len(seq)):
      # ignore numbers with a leading 0
      if seq[curIdx] == '0' and i != curIdx:
        break

      # grab 1+ chars for processing
      segment = seq[curIdx: i + 1]
      segmentVal = int(segment)

      # a binary operator needs 2 operands and this is
      # the first index so simply send the segment's segmentVal
      if curIdx == 0:
        calcuateExpr(curExpr + segment, seq, target, i + 1, segmentVal)
      else: # try (+) and (-) each time
        calcuateExpr(curExpr + "+" + segment, seq, target, i + 1, total + segmentVal)
        calcuateExpr(curExpr + "-" + segment, seq, target, i + 1, total - segmentVal)

  calcuateExpr(curExpr="", seq=seq, target=target, curIdx=0, total=0)




print(printExprs("32", 5))
