"""
check list is permutation. 
data: trevel route
distance: travel distance
For example
  A[0] = 1
  A[1] = 3
  A[2] = 2
  A[3] = 4

return 1

For example:
  A[0] = 1
  A[1] = 4
  A[2] = 3
 
return 0 it is not a permutation list because 2 is missing
"""


def validate(data: list):
    data.sort()
    count = 1
    for i in data:
        if count == i:
            count += 1
        else:
            return 0
            
    return 1
        

assert validate([1,2,3,4]) == 1
assert validate([1,2,4]) == 0
assert validate([4,3,2,5]) == 0
assert validate([4,2,3,1,5]) == 1
