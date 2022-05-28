# https://leetcode.com/problems/text-justification/

def fullJustify(words, maxWidth):
  result, current, numLetters = [], [], 0
  for word in words:
    if len(current) + len(word) + numLetters > maxWidth:
        #if current line only has one word
      if len(current) == 1:
        result.append(current[0] + " "*(maxWidth-numLetters))

      else: #otherwise add in spaces between words and append to result
        numSpaces = maxWidth - numLetters
        spaceBetween, numExtraSpaces = divmod(numSpaces, len(current)-1)

        #round robin adding extra spacing
        for i in range(numExtraSpaces):
            current[i] += ' '
        result.append((' '*spaceBetween).join(current))
      #reset current line and number of letters after last line was added
      current, numLetters = [], 0
      #add next word to current line and get length of next word
    current += [word]
    numLetters += len(word)
  #add final line to result with necessary extra spaces at the end of line
  result.append(' '.join(current) + ' '*(maxWidth - numLetters - len(current) + 1))
  return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(fullJustify(words, maxWidth))
# ['This    is    an', 'example  of text', 'justification.  ']
