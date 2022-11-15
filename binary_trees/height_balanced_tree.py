def solution(array):
    return sortedArrayToBSTHelper(array, 0, len(array) - 1)
    
def sortedArrayToBSTHelper(nums, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    root = Tree(nums[mid])
    root.left = sortedArrayToBSTHelper(nums, start, mid - 1)
    root.right = sortedArrayToBSTHelper(nums, mid + 1, end)
    return root
