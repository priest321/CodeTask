
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