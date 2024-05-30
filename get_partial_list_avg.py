"""
find the min slice position and mini slice avg values
example 
_____________________
[1,2,1,1] should return (2, 1.0)
posible slice could be [1,2] = (1+2)/2 = 1.5, [2,1] = (2+1)/2 = 1.5, [1,1] = (1+1)/2 = 1,
[1,2,1] = (1+2+1)/3 = 4/3, [2,1,1] = (2+1+1)/3 = 4/3, [1,2,1,1] = (1+2+1+1) = 1.25 
return index 2 and mini avg is 1.0

[5,2,2,5,1,5] should return (1, 2.0)
posible slice could be [5,2], [2,2], [2,5], [5,1], [1,5], [5,2,2], [2,2,5], [2,5,1], [5,1,5],
[5,2,2,5], [2,2,5,1], [2,5,1,5], [5,2,2,5,1], [2,2,5,1,5], [5,2,2,5,1,5], 
"""

def solution(A: list):

    size = len(A)
    min_sum = float("inf")
    index = None
    for i in range(size-1):
        pair_sum = (A[i] + A[i+1]) / 2.0
        
        # two pair
        if min_sum > pair_sum:
            min_sum = pair_sum
            index = i
            
        # there pair
        if i < size -2:
            there_element_sum = (A[i] + A[i+1] + A[i+2]) / 3.0
            if min_sum > there_element_sum:
                min_sum = there_element_sum
                index = i
                
    return index, min_sum
    


print(solution([4, 2, 2, 5, 1, 5, 8]))
assert solution([4, 2, 2, 5, 1, 5, 8]) == (1, 2.0)  # Should return 1
