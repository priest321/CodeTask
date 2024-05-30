"""
process the list, list start with number of 0: list = [0,0,0,0]

two way process the list
1. increase one if number <= len(list)
    data[0] = 3  list from [0,0,0,0] to [0,0,1,0]
    data[1] = 2  list from [0,0,1,0] to [0,1,1,0]
    data[2] = 3  list from [0,1,1,0] to [0,1,2,0]
    
2. flat the list if number > len(list):
    data[3] = 5  list from [0,1,2,0] to [2,2,2,2]
    
"""


def process(number: int, data):
    init_data = [0 for i in range(number)]
    max_num = 0
    for d in data:
        if d <= number:
            init_data[d-1] += 1
            if init_data[d-1] > max_num:
                max_num = init_data[d-1]
        else:
            init_data = [max_num for i in range(number)]
            
    return init_data
        

assert process(4, [1,2,3,4]) == [1,1,1,1]
assert process(3, [1,2,2,4]) == [2,2,2]
assert process(5, [4,4,4,9]) == [3,3,3,3,3]