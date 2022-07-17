# # https://www.algoexpert.io/questions/Water%20Area
# We can actually also solve this question with constant space (see our written Solution 2).

# To do so, we have to realize that, if we just look at the two extremeties of the input array, the smaller of the two values gives us information about water to be trapped in the middle. For example, consider the following simple array:

# heights = [4, 0, 6, 0, 10]
# Since the leftmost value 4 is smaller than the rightmost value 10, we know that, assuming all values in between are smaller than this leftmost value, we'll trap water equal to the difference between 4 and those values.

# Now of course, middle values won't always be smaller than the leftmost value, like the middlemost value in the array above which is 6. In those cases, we update the leftmost value, making the leftmost value effectively contain the greatest most recently visited value to the left.

# Broadly speaking, the algorithm works by setting up two pointers—a left and right pointer—at the extremities of the input array and progressively pushing the one that points to the smallest value inward. At each value in between the pointers, we update the relevant left-or-right max value (this depends on which pointer we moved inward), and we add to our final surface area the difference between the relevant left-or-right max value and the current value. We repeat this until the left and right pointers pass each other.

# Since we only need to store five values, this algorithm only requires constant space.


def waterArea(heights):
    if len(heights) == 0:
        return 0

    leftIdx = 0
    rightIdx = len(heights) - 1
    leftMax = heights[leftIdx]
    rightMax = heights[rightIdx]
    surfaceArea = 0

    while leftIdx < rightIdx:
        if heights[leftIdx] < heights[rightIdx]:
            leftIdx += 1
            leftMax = max(leftMax, heights[leftIdx])
            surfaceArea += leftMax - heights[leftIdx]
        else:
            rightIdx -= 1
            rightMax = max(rightMax, heights[rightIdx])
            surfaceArea += rightMax - heights[rightIdx]
    return surfaceArea
