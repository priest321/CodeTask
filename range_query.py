"""
rotation array:
example 
_____________________
<input> is a list of integer and number of steps
exmaple
(3, [1,2,3,4]) -> [4, 1, 2, 3]
3 indicate rotate 3 times
first time   [1,2,3,4] -> [4,1,2,3]
second times  [4,1,2,3] -> [3,4,1,2]
Third times   [3,4,1,2] -> [2,3,4,1]

"""

def rotation_array(step: int, data: list):
    size = len(data)
    if not data:
        return data
        
    step = step % size
    return data[-step:] + data[:size-step] if step else data

print(rotation_array(3, [1,2,3,4]))
assert rotation_array(3, [1,2,3,4]) == [2,3,4,1]
assert rotation_array(4, [1,2,3,4]) == [1,2,3,4]
