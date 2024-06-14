# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:12:30 2024

@author: pries

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60
"""


def solution(A) -> int:
    
    triplet_max = [float('-inf'), float('-inf'), float('-inf')]
    triplet_min = [float('inf'), float('inf')]
    
    for i in A:
        if [k for k in triplet_max if k < i]:
            triplet_max.append(i)
            triplet_max.sort()
            triplet_max.pop(0)
            
        if [l for l in triplet_min if l > i]:
            triplet_min.append(i)
            triplet_min.sort()
            triplet_min.pop()
    
    result: list = []
    total_1: int = 1
    
    for v in triplet_max:
        total_1 *= v

    total_2: int = 1
    for t in triplet_min:
        total_2 *= t
        
    total_2 = total_2*triplet_max[-1]   
    result.extend([total_1, total_2])
    
    return max(result)

print(solution([-3, 1, 2, -2, 5, 6]))
print(solution([-3, 1, 2, -2, -5, -6]))
print(solution([-5, -6, -4, -7, -10]))
print(solution([4, 7, 3, 2, 1, -3, -5]))