"""
5. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes
 (i.e., only nodes themselves may be changed).

### Example 1:
**Input:** head = [1,2,3,4]  
**Output:** [2,1,4,3]

### Example 2:
**Input:** head = []  
**Output:** []

### Example 3:
**Input:** head = [1]  
**Output:** [1]

### Constraints:
- The number of nodes in the list is in the range [0, 100].
- \( 0 \leq \text{Node.val} \leq 100 \)

"""

def swap_node(data: list):
    size = len(data)
    for i in range(0, size-1, 2): # check old number
        data[i], data[i+1] = data[i+1], data[i]
    return data


assert swap_node([1,2,3,4]) == [2,1,4,3]
assert swap_node([5,6,2,1]) == [6,5,1,2]
assert swap_node([1,2,3]) == [2,1,3]
assert swap_node([1,2,3,4,5,6,7,8,7,6,5,4]) == [2,1,4,3,6,5,8,7,6,7,4,5]