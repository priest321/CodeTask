# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:55:19 2024

@author: pries
"""

import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(2)  # Pause for 2 seconds
    print("Task 1: After 2 seconds")

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(1)  # Pause for 1 second
    print("Task 2: After 1 second")

async def main():
    print("Main: Start")
    
    # Schedule the tasks to run concurrently
    await task1()
    await task2()
    
    print("Main: Done")

# Run the main function
asyncio.run(main())
    