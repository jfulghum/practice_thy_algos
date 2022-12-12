def sortColors(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      low = 0
      high = len(nums) - 1
      mid = 0 # mid must be the same as low 

      while mid <= high:
          if nums[mid] == 0:
              nums[low], nums[mid] = nums[mid], nums[low]
              low += 1
              mid+=1
          elif nums[mid] == 2:
              nums[high], nums[mid] = nums[mid], nums[high]
              high -= 1
              #do not increment mid here
          else:
              mid += 1
              
              
              
# Test cases
tests = [
 ([2, 1, 2, 1, 0], [0, 1, 1, 2, 2]),
 ([0, 1, 2, 1], [0, 1, 1, 2]),
 ([0, 1], [0, 1]),
 ([], [])
]

# Should print out results for each test
for params, expected in tests:
  actual = sort_colors(params)
  if actual != expected:
    print(f"Test failed for {params}. Expected: {expected}, Actual: {actual}")
  else:
    print(f"Works fine for {params}.")

