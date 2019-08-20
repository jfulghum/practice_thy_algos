
list1 = [0,0,1,1,1,2,2,3,3,4] #5
list2 = [0,0,1,1,1,2,2,3,3,4]
#list is sorted, but do it in O(1) memory
def removeDups(nums):
  i = 0
  for j in (range(1,len(nums))):
    if nums[j] != nums[i]:
      print(nums[j], nums[i], nums)
      i += 1
      nums[i] = nums[j]
  return i + 1

print(removeDups(list1))

list2 = [3,2,2,3] # 2
val = 3
def removeElement(nums, val):
  i = 0
  for j in range(1, len(nums)):
    if nums[j] != val:
      nums[i] = nums[j]
      i += 1
  return i

print(removeElement(list2, val))








