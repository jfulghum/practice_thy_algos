def remove_extra_consecutive(input_str, max_consecutive_chars):
  output = ""
  consecutive_count = 0
  prev_char = None
  for current_char in input_str:
    if prev_char == current_char:
      consecutive_count += 1
    else:
      consecutive_count = 0
      prev_char = current_char
    if consecutive_count < max_consecutive_chars:
      output += current_char
  return output

print(remove_extra_consecutive("johanna", 1))
