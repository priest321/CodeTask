def binary_search(data:list, target):
    def search(partial_data, target):
        if not partial_data:
            return False
            
        size = len(partial_data)
        mid = size//2
        print(partial_data, target, mid)
        if partial_data[mid] == target:
            return True
        elif partial_data[mid] < target:
            return search(partial_data[mid:], target)
        else:
            return search(partial_data[:mid], target)
    
    return search(data, target)
	


print(binary_search([1], 1))
print(binary_search([1,2], 1))
print(binary_search([1,2,5,9], 5))

print(binary_search([1,2,3,4,5,6,7,8,9], 5))

print(binary_search([1,2,3,4,5,7,8,9,10,11], 6))