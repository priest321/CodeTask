"""
Compute number of integers divisible by k in range [a..b].

example 
_____________________
start 5, end 10, value 2 should return len([6, 8, 10]) = 3 

"""

def divisiable_value(start: int, end: int, gap:int):
    # small range
    #return len([i for i in range(start, end+1) if i % value == 0])
    
    # large range
    count_A = (start-1) // gap if start >= 1 else start // gap
    count_B = end // gap
    return count_B - count_A


assert divisiable_value(5, 10, 2) == 3
assert divisiable_value(4, 10, 2) == 4
assert divisiable_value(4, 9, 2) == 3
assert divisiable_value(0, 31, 15) == 2
assert divisiable_value(11, 345, 17) == 20
assert divisiable_value(0, 1, 17) == 0