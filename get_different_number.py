def get_different_number(arr):
  sorted_arr = sorted(arr)
  for i in range(len(sorted_arr)):
    if i != sorted_arr[i]:
      return i
  return len(arr)


def get_different_number2(arr):
  set1 = set(arr)
  for i in range(len(arr)):
    if i not in set1:
      return i
  return len(arr)
