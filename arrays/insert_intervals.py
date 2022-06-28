
# https://leetcode.com/problems/insert-interval/solution/
# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

#Pitfalls:
#You must ask and make sure it is sorted.
# Come up with test cases (as few as possible that covered everything, don't waste your interview time):

# [1, 5],[3, 6] => [1, 6]
# [1, 5], [2, 3]
# [1, 5], [5, 6]
# [6, 7], [1, 4], [2, 3], [4, 5]

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
            
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)
        
        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
