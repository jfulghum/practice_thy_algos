
def bubbleSort(array, n):
 
    for i in range(n - 1):
        if array[i] > array[i + 1]:
           [array[i], array[i+1]] = [array[i + 1], array[i]]
 
    if n - 1 > 1:
        bubbleSort(A, n - 1)
 
 

A = [ 3, 5, 8, 4, 1, 9, -2 ]

bubbleSort(A, len(A))
