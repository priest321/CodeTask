# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:03:01 2024

@author: pries
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
A[0] = 1
A[1] = 5
A[2] = 2
A[3] = 1
A[4] = 4
A[5] = 0
"""

def solution(data: list) -> int:
	# start list [] holding all start point
	# end list [] holding all end point
	# stack start point count += stack all start point if that not end yet
	size = len(data)
	start_points: list = [(i-data[i]) for i in range(size)]
	end_points: list = [(i+data[i]) for i in range(size)]
	
	start_points.sort()
	end_points.sort()
	
	print(start_points)
	print(end_points)
	
	stack: list = []
	count = 0
	
	end_index = 0
	
	for i in range(size):
		# remove disc from stack if start point aleady passed end point
		while end_points and (end_points[end_index] < start_points[i]):
		
			end_index += 1
			stack.pop(0)
			
		count += len(stack)
		stack.append(start_points[i])
	return count

print(solution([1,5,2,1,4,0]))
assert solution([1,5,2,1,4,0]) == 11