def nextGreaterElement(nums1, nums2):
  ans = []
  for x in nums1:
      j = nums2.index(x)
      found = False
      
      while j < len(nums2) - 1:                
          if x < nums2[j+1]:
              ans.append(nums2[j+1])
              found = True
              break
          j += 1
          
      if found == False:
          ans.append(-1)
  
  return ans

nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1, nums2)) # [-1, 3, -1]
