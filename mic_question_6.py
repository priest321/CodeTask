# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:29:05 2024

@author: pries
"""

def solution(data: str, gap: int) -> str:
	# 1. get most popular dictionary 
	# 2. create a list with (times: char) then sort list with desc order
	# 3. create a list check what is the next avaiable index for used char
	# 4. if all checked without char add into the list add idle
    data = list(data)
    output: list = []
    valid_index_mapping: dict = {}
    
    def get_best_char(data, gap, valid_index_mapping, output):
        
        char_count: dict = {}
        ordered_list: list = []
        
        for d in data:
            if d not in char_count:
                char_count[d] = 1
            else:
                char_count[d] += 1
                
        for k, v in char_count.items():
            ordered_list.append((v, k))
            
        ordered_list.sort(reverse=True)
        size: int = len(ordered_list)
    
        for k, v in ordered_list:
            if v not in valid_index_mapping or (v in valid_index_mapping and (len(output)) >= valid_index_mapping[v]):
                output.append(v)
                valid_index_mapping[v] = len(output) + gap-1
                data.remove(v)
                return output
            
        return output.append("idle")
    limited = 0
    
    while data:
        get_best_char(data, gap, valid_index_mapping, output)
            
    return "->".join(output)
    
assert solution("aaabcc", 3) == 7