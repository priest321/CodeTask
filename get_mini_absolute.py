"""
find the absolute difference between the sum of the <first part> and the sum of the <second part>.
example:

[1,2,3,4]
first part can be [1] second part [2,3,4] absolute is "|(1) - (2+3+4)| = 8" or
first part can be [1,2] second part [3,4] absolute is "|(1+2) - (3+4)| = 4" or
first part can be [1,2,3] second part [4] absolute is "|(1+2+3) - (4)| = 1"
so that minimal absolute different is 1
return 1
"""


def get_mini_absolute(data: list):
    total_sum = sum(data)
    left_sum = 0
    best_result = float('inf')
    for i in range(len(data)-1):
        left_sum += data[i]
        current_result = abs(2*left_sum - total_sum)
        if current_result < best_result:
            best_result = current_result
        
    return best_result
 
    
assert get_mini_absolute([3,1,2,4,3]) == 1
assert get_mini_absolute([1,2,3,4,5]) == 3
assert get_mini_absolute([6,5,3,4,5,6]) == 1
assert get_mini_absolute([6,5,3,4,5,99999]) == 99976
assert get_mini_absolute([-10, -20, -30, -40, 100]) == 20
print(get_mini_absolute([1, 2, 3, 4, 2]))
assert get_mini_absolute([1, 2, 3, 4, 2]) == 0

