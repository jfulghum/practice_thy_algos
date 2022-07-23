def underscorifySubstring(string, substring):
  idx_open = -1
  idx_close = -1
  idx = 0
  finalChars = ""
  while idx <= len(string) - len(substring):
    curr = string[idx:idx+len(substring)]

    if curr == substring:
      if idx_open < 0:
        finalChars += "_"
        idx_open = idx
      idx_close = idx + len(substring)
    elif idx == idx_close:
      finalChars += "_"
      idx_open = -1
      idx_close = -1

    finalChars += string[idx]
    idx += 1

  if idx_close > 0:
    while idx < idx_close:
      finalChars += string[idx]
      idx += 1
    finalChars += "_"
  finalChars += string[idx:]

  return finalChars

print(underscorifySubstring("testthis is a testtest to see if it works testestest", "test"))
# _test_this is a _testtest_ to see if it works _testestest_

print(underscorifySubstring("testestest", "test"))
