"""
3. Merge k Sorted Lists

You are given an array of ( k ) linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Example 1:
**Input:** lists = [[1,4,5],[1,3,4],[2,6]]  
**Output:** [1,1,2,3,4,4,5,6]  
**Explanation:** The linked-lists are:
```
1 -> 4 -> 5,
1 -> 3 -> 4,
2 -> 6
```
Merging them into one sorted list:
```
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

### Example 2:
**Input:** lists = []  
**Output:** []

### Example 3:
**Input:** lists = [[]]  
**Output:** []

### Constraints:
- ( k == lists.length )
- ( 0 leq k leq 10^4 )
- ( 0 leq lists[i].length leq 500 )
- ( -10^4 leq lists[i][j] leq 10^4 )
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed ( 10^4 ).


"""
import heapq
import typing

def merge_all_sort_list(data: list):
    final = []
    for d in data:
        final.extend(d)
    final.sort()
    return final
    

assert merge_all_sort_list([[1,4,5],[1,3,4],[2,6]]) == [1,1,2,3,4,4,5,6]
assert merge_all_sort_list([]) == []
assert merge_all_sort_list([[]]) == []

