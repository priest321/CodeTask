# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:58:50 2024

@author: pries
"""
def solution(data:list) -> list:
	# 1. set "one" keep any new value 
	# 2. set "two" keep value duplicated 
	# 3. get different from set one to set two
	set_one = set()
	set_two = set()
	
	if not data:
		return set_one
		
	for value in data:
		if value not in set_one:
			set_one.add(value)
		else:
			set_two.add(value)
			
	return set_one.difference(set_two)

			
assert solution([2,3,4,5,4,5]) == {2,3}
assert solution([0]) == {0}
assert solution([-1]) == {-1}
assert solution([1,2]) == {1,2}
assert solution([]) == set()