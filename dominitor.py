"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions
"""


def dominitor(data):
    edge = len(data)//2  # compare should bigger t
    mapping = {}
    for d in data:
        if d not in mapping:
            mapping[d] = 1
        else:
            mapping[d] += 1
        if mapping[d] > edge:
            return d
    return -1
    


assert dominitor([2]) == 2
assert dominitor([-2]) == -2
assert dominitor([3,4,3,2,3,-1,3,3]) == 3
assert dominitor([3,4,3,2,3,-1,3,3,4]) == 3

assert dominitor([-1]) == -1 
assert dominitor([]) == -1
assert dominitor([1,2,3,4]) == -1
assert dominitor([2,1]) == -1

        
    
    