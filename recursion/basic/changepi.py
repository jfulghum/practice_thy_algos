# https://replit.com/@jfulghum/UnfoldedNegligibleSystemintegrator#main.py

def changePi(string):
  for i in range(len(string) - 2):
    if string[i:i+2] == "pi":
      string = string[:i] +  "3.14" + string[i+2:]
  return string



def changePi(word: str) -> str:
  print(word)
  if len(word) <= 1:
    return word

  if word[0:2] == "pi":
    return "3.14" + changePi(word[2:])

  return str(word[0]) + changePi(word[1:])



print(changePi("xpix") == "x3.14x")
# print(changePi("pipi") == "3.143.14")
# print(changePi("pip") == "3.14p")
