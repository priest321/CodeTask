# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:20:09 2024

@author: pries
For example, the string "{[()()]}" is properly nested but "([)()]" is not.
S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0
"""



def solution(S):

    front_symbol: list = ["{", "(", "["]
    mapping: dict = {
        "}": "{",
        ")": "(",
        "]": "["
        }
    
    collector: list = [] 
    for symbol in S:
        if symbol in front_symbol:
            collector.append(symbol)
        elif collector:
            last_symbol = collector.pop()
            if last_symbol != mapping.get(symbol):
                return 0
        

    return 1 if not collector else 0


print(solution(')('))
print(solution('()()'))
print(solution('{()()}'))