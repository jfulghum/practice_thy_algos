def chain(arr, i, n, prev):
 
        if i == n:
            return 0
    
        # case 1: exclude the current element and process the
        # remaining elements
        excl = chain(arr, i + 1, n, prev)
    
        # case 2: include the current element if it is greater
        # than the previous element in LIS
        incl = 0
        if arr[i] > prev:
            incl = 1 + chain(arr, i + 1, n, arr[i])
    
        return max(incl, excl)


def solution(arr):
    return chain(arr, 0, len(arr), float('-inf'))

