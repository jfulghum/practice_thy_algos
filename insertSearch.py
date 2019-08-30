def searchInsert(nums, target):
    if len(nums) == 0:
        return 0
    for i, el in enumerate(nums):
        if el >= target:
            return i
    return len(nums)
