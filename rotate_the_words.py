"""
“Rotate the words in this string”
  0      1    2    3  4      5

  2      3    4    5  0      1

actual rotations = k % num words
new index = (current index + actual rotations) % num words

(4 + 2) % 6 == 0
(5 + 2) % 6 == 1

"""

def rotateByK(input, k):
    words = input.split(" ")
    rotated_words = [0 for x in words]
    for i in range(len(words)):
        new_index = (i + k) % len(words)
        rotated_words[new_index] = words[i]
    return " ".join(rotated_words)
