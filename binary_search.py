def search(data, target):
    def binary_search(data, low, high, t):
        if high>=low:
            mid = (low+high)//2
            if data[mid] == t:
                return mid
            elif data[mid] < target:
                return binary_search(data, mid+1, high, t)
            else:
                return binary_search(data, low, mid-1, t)
        else:
            return -1
    return binary_search(data, 0, len(data)-1, target)
	


print(search([1], 1))
print(search([1,2], 1))
print(search([1,2,5,9], 5))

print(search([1,2,3,4,5,6,7,8,9], 5))

print(search([1,2,3,4,5,7,8,9,10,11], 6))







