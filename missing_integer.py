"""

Find the smallest positive integer that does not occur in a given sequence
example 
_____________________
<input> is a list of integer and number
exmaple
[1,2,3,4,6,6] return 5
[-1,-3] return 1
[] return 1
[1,2,3] return 4
"""

def get_missing_integer(data: list):
    data = list({i for i in data if i > 0})
    
    num = 1
    
    for i in data:
        if i == num:
            num +=1
        elif i != num:
            break
    
    return num


assert get_missing_integer([1,2,3,4]) == 5
assert get_missing_integer([1,2,3,5]) == 4
assert get_missing_integer([]) == 1
assert get_missing_integer([-1]) == 1
assert get_missing_integer([9]) == 1
assert get_missing_integer([1, 3, 6, 4, 1, 2]) == 5
assert get_missing_integer([1, 2, 3, 3, 4]) == 5
