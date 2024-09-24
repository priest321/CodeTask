# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:20:36 2024

@author: pries
"""

import pandas as pd
import numpy as np


PATH = "data/basic_data.xlsx"


class DataModule:
    def __init__(self, name):
        self.name = name
        self.data = None
        self.numbers = []
        
    @property
    def load_data(self):
        self.data = pd.read_excel(PATH)
        print(type(self.data))
        
    @property
    def processing_data(self):
        print(self.data)
        print("describe", self.data.describe())
        print("_________________________________\n")
        print("info", self.data.info())
        print("_________________________________\n")
        print("to numpy", self.data.to_numpy())
        print("_________________________________\n")
        print("location: \n", self.data["Location"])
        print("_________________________________\n")
        print("location: \n", self.data["Date"])
        print("_________________________________\n")
        for i in range(len(self.data)):
            row = self.data.iloc[i]
            print(row["Date"], row["Location"])
            
                
        
    def output_data(self):
        pass
    
    

model_one = DataModule("xml")
print(model_one.name)
model_one.load_data
model_one.processing_data
