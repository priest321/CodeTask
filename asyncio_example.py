# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:37:39 2024

@author: pries
"""
import asyncio


def debug_message(func):
    def warper(*args, **kargs):
        print(f"execute function: {func.__name__}")
        result = func(*args, **kargs)
        if result:
            print(f"{func.__name__} return result: {result}")
            return result
    return warper


@debug_message
def call_back(result):
    if result == 1:
        print("3 Correct")
    else:
        print("Incorrect")
        
            
class LoopEvent:
    def __init__(self, loop):
        self.loop = loop
        self.trigger_event()
        
    def trigger_event(self):
        self.loop.run_until_complete(self.processing())
        
    async def processing(self):
        print("1 hello world")
        await asyncio.gather(self.count(call_back), self.delay_function())
        print("5 end process")
        
    @debug_message
    async def count(self, call_back_func):
        await asyncio.sleep(5)
        call_back_func(1)
        print("4 End count function")
        return "count"

    @debug_message
    async def delay_function(self):
        await asyncio.sleep(3)
        print("2 End delay function")
        return "delay function"



if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop_event = LoopEvent(loop)
    loop.run_forever()