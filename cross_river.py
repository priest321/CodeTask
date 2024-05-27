"""
count minimal number of jumps. 
data: trevel route
distance: travel distance
For example, you are given integer X = 3 and array data such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  
return 4 because 1,2,3 all precent at A[4] index

For example, you are given integer X = 5 and array data such that:
  A[0] = 1
  A[1] = 4
  A[2] = 3
  A[3] = 2
  A[4] = 3
  A[5] = 5
  
return 5 because 1,2,3,4,5 all precent at A[5] index
"""


def get_jumps(data: list, distance: int):
    
    distance = [i for i in range(1, distance+1)]
    for i in range(len(data)):
        if data[i] in distance:
            distance.remove(data[i])
        if not distance:
            return i
    
    return -1

assert get_jumps([1,3,1,4,2,3,5], 5) == 6
assert get_jumps([1,2,3,4,2,3,5], 4) == 3
assert get_jumps([1,4,3,2,3,5], 5) == 5
assert get_jumps([1], 5) == -1
