"""
count the number of passing cars on the road
example 
_____________________
data = [0,1,0,1,1] return 5
because count index 0 got index 1, index 3, index 4 passing index 2 got index 3 and index 4 passing


"""

def get_passing(data: list):
    num_of_car = 0
    passing = 0
    for d in data:
        if d == 0:
            num_of_car += 1
        elif d == 1:
            passing += num_of_car
    return passing

assert get_passing([0,1,0,1,1]) == 5
assert get_passing([0,1,0,1,1,1]) == 7
assert get_passing([0,1,0,1,1,1,0,1]) == 10