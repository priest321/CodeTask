# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:08:26 2024

@author: pries
that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:
 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3
"""

def solution(A):
    return len({i for i in A})


assert solution([1,2,3,4,3,2,1]) == 4
assert solution([1,2,3,4,3,2,5,2,3,2,1]) == 5
