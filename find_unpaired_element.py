"""
Find unpaire element
The array contains an odd number of elements, 
and each element of the array can be paired with another 
element that has the same value, except for one element 
that is left unpaired.
[1,1,9,4,4,6,7,9,6] return 7
[1,1,9,4,4,6,7,9,7] return 6
"""

def find_unpaired_element(data: list):
    data.sort()
    size = len(data)
    for i in range(0, size, 2):
        if i == size-1:
            return data[i]
        elif data[i] != data[i+1]:
            return data[i]
    
    return 0

assert find_unpaired_element([1,1,2,2,3,3,4,4,5]) == 5
assert find_unpaired_element([1,1,9,4,4,6,7,9,6]) == 7
assert find_unpaired_element([1,1,9,4,4,6,7,9,7]) == 6
