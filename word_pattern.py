string = "jo han jo han"
pattern = "abab"

def word_pattern(string, pattern):
  words = string.split(" ")
  if len(words) != len(pattern):
    return False
  return list(map(pattern.find, pattern)) == list(map(words.index, words))

print(word_pattern(string, pattern))
