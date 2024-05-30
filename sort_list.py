"""
sort the list with ascending orders
"""

def sort_list(data: list):
    condition = True
    def compare(data):
        keep_going = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                keep_going = True
        return keep_going
        
    while condition:
        condition = compare(data)
        
    print(data)
    return data

assert sort_list([1,2,3,4,5,9,8,7,6,4,5,4,3,2,1])

