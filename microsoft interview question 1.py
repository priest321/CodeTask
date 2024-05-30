"""
1. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size \( m \) and \( n \) respectively, return the median of the two sorted arrays.

The overall run time complexity should be \( O(\log (m+n)) \).

### Example 1:
**Input:** nums1 = [1, 3], nums2 = [2]  
**Output:** 2.00000  
**Explanation:** merged array = [1, 2, 3] and median is 2.

### Example 2:
**Input:** nums1 = [1, 2], nums2 = [3, 4]  
**Output:** 2.50000  
**Explanation:** merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.

### Constraints:
- nums1.length == m
- nums2.length == n
- \( 0 \leq m \leq 1000 \)
- \( 0 \leq n \leq 1000 \)
- \( 1 \leq m + n \leq 2000 \)
- \( -10^6 \leq nums1[i], nums2[i] \leq 10^6 \)


"""

def get_median(data1: list, data2: list):
    data1.extend(data2)
    data1.sort()
    size: int = len(data1)
    if size:
        mid_index: int = size//2
        
        if size % 2:
            return data1[mid_index]
        else:
            return (data1[mid_index] + data1[mid_index-1])/2


assert get_median([1,2,3,6], [8,9,10]) == 6.0
assert get_median([1,3], [2]) == 2.0
assert get_median([1,2], [3,4]) == 2.5
assert get_median([], []) == None
assert get_median([1], []) == 1
