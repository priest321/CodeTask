# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:11:49 2024

@author: pries
"""


def process(func):
    def warper(*args, **kwargs):
        try:
            func_name = func.__name__
            print(f"processing function {func_name} args{type(args)}")
            args = (k for k in args)
            print(args)
            result = func(*args, **kwargs)
            if result:
                print(f"processed function {func_name} with result {result}")
            return result
        except Exception as e:
            print(f"Processing function {func_name} raised error: {e}")
    return warper

@process
def get_num_list(num):
    return [i for i in range(num)]



print(get_num_list(5))