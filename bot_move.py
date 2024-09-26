
def solution(data: list, valid: list) -> bool:
    size = len(data)
    data_index = [i for i in range(size) if data[i] == 1]
    valid_index = [v for v in range(size) if valid[v] == 1]
    
    for i in range(len(data_index)):
        if abs(data_index[i] - valid_index[i]) > 1:
            return False
            
    return True
	
	
assert solution([1,0,0,1], [0,1,1,0]) == True
assert solution([1,0,0,0,1], [1,0,1,0,0]) == False
assert solution([1,1,0,0,1], [1,0,1,0,1]) == True
assert solution([1,0,0,0,0], [1,0,0,0,0]) == True

def solution(data1, data2) -> bool:
    positions = [i for i in range(len(data1)) if data1[i] == 1]
    moved_positions = [i for i in range(len(data2)) if data2[i] == 1]
    if len(positions) == len(moved_positions):
        for i in len(positions):
            if abs(moved_positions[i] - positions[i]) > 1:
                return False
        return True
    else:
        return False
    