# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:11:49 2024

@author: pries
"""


class Car:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
car1 = Car("BYD")

print(car1.get_name())
print(car1.__class__.__name__)


def process(func):
    def warper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"processing func {func.__name__} with result {result}")
        return result
    return warper

@process
def get_num_list(num):
    return [i for i in range(num)]



get_num_list(5)