def solution(array1, array2):
    arr = array1 + array2
    arr.sort()
    n = len(arr)
 
    if n % 2 == 0:
        mid = n // 2
        left = arr[mid]
        right = arr[mid - 1]
        return (left + right) / 2
         
    else:
        mid = n // 2
        return arr[mid]
        
    
