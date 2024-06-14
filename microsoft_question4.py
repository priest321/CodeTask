"""
4. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list \( k \) at a time, and return the modified list.

( k ) is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of \( k \), then the left-out nodes, in the end, should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

### Example 1:
**Input:** head = [1,2,3,4,5], ( k = 2 )  
**Output:** [2,1,4,3,5]

### Example 2:
**Input:** head = [1,2,3,4,5], ( k = 3 )  
**Output:** [3,2,1,4,5]

### Constraints:
- The number of nodes in the list is ( n ).
- ( 1 leq k leq n leq 5000 )
- ( 0 leq text{Node.val} leq 1000 )

"""

def Reverse_node(data: list, distance: int) -> list:
    size: int = len(data)
    for i in range(0, size-distance, distance):
        temp = data[i:i+distance]
        temp.reverse()
        data[i:i+distance] = temp
        print(data)

    return data

    
assert Reverse_node([1,2,3,4,5], 2) == [2,1,4,3,5]
assert Reverse_node([1,2,3,4,5], 3) == [3,2,1,4,5]
