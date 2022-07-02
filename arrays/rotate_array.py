# Today, we will be rotating all elements in an array by k positions. This isn't a difficult problem, but the in-place O(1) space solution isn't apparent.

# https://replit.com/@jfulghum/MellowUnlinedEquations#main.py
# 1, 2, 3, 4, k = 1 => 2, 3, 4, 1


def rotate(nums, k):
    # size = len(nums)
    # rotated = [None] * size
    # i = 0
    # rotated_index = k
    # while rotated_index < size:
    #     rotated[i] = nums[rotated_index]
    #     i += 1
    #     rotated_index += 1
    # rotated_index = 0
    # while rotated_index < k:
    #     rotated[i] = nums[rotated_index]
    #     i += 1
    #     rotated_index += 1
    # return rotated
    k = k % len(nums)
    l, r = 0, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l, r = 0, k-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l, r = k, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums



print(rotate([1, 2, 3, 4], 1) == [4, 1, 2, 3])
print(rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3])
print(rotate([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3])
