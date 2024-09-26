"""
count minimal number of jumps from position X to Y. 
start : start point
end : end point
jump_size : travel distance:
example:
if start point is 10, end point is 85, each time travel distance is 30
after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
"""


def get_jumps(start: int, end: int, jump_size:int):
    
    if start > end:
        return 0
        
    distance = end - start
    
    return distance//jump_size+1 if distance % jump_size else distance//jump_size
    

assert get_jumps(10, 85, 30) == 3
assert get_jumps(100, 9000, 100) == 89
assert get_jumps(1, 10, 3) == 3


def get_jumps(start, end, distance) -> int:
    if start > end:
        return 0
        
    travel = (end - start) / distance
    if int(travel) < travel:
        return int(travel) + 1
    else:
        return int(travel)