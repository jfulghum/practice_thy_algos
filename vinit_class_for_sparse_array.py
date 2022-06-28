'''

You are given a large array where the vast majority of the elements is zero. Create a class that can store these elements more space efficiently. Your class must have the following methods:

init(original) - you are passed in the original array
set(i, val) - set the value val at index i
get(i) - get the value at index i

[0, 0, 0, 0, 0, .... , 1, 0, 0, 0 ... 7]

arr[i] = val

Edge case:
you set it to 5 and then 0:
set(0, 5)
set(0, 0)
get(0) => 0


Time complexity 
Is O(n) n being size of array 

Set method is O(1)
Get method is O(N)

Space Complexity of the Class:


'''

from typing import Set


class Array:

    def __init__(self, original):

        self.max_index = len(original) - 1
        self.map = self.convert_list_to_map(original)

    def convert_list_to_map(self, original):

        map = {}
        for i in range(len(original)):
            if original[i] != 0:
                map[i] = original[i]
        return map

    def set(self, i, val):
        if i >= 0 and i <= self.max_index:
            if val != 0:
                self.map[i] = val
            elif self.map.get(i):
                del self.map[i]
        else:
            raise Exception("Index out of bounds")
        
    def get(self, i):
        if i >= 0 and i <= self.max_index:
            return self.map[i] if i in self.map else 0
        else:
            raise Exception("Index out of bounds")
