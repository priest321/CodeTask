"""  
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish  and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

        0 represents a fish flowing upstream,
        1 represents a fish flowing downstream.

If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

        If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
        If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.

We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.
A[0] = 4    B[0] = 0
A[1] = 3    B[1] = 1
A[2] = 2    B[2] = 0
A[3] = 1    B[3] = 0
A[4] = 5    B[4] = 0
"""

def get_remaining_fish(A, B) -> int:
    # true: if 0 count +1 from list left until find 1
    # <1> option meet bigger fish -> die, <2> eat until meet another 1 add to temp list 
    # <option1> win then we need <count> temp list other wise count "0" <direction fish>
	
    assert len(A) == len(B)
	
    size: int = len(A)
    temp: list = []
    count: int = 0
    fishes: list = []  # for debug only
	
    def fight(challenge_fish: int, temp: list, fish_name: list):
        for index in range(len(temp)):
            if temp[-1] > challenge_fish:
                return 0  # temp fishes won
            else:  # there is not same size fish and fish will not growing after having a meal
                temp.pop()
				
        fish_name.append(challenge_fish)
        return 1  # chellenge fish won
					
    for i in range(size):
        if B[i] == 0 and not temp:
            count += 1
            fishes.append(A[i])
        elif B[i] == 1:
            temp.append(A[i])
        elif B[i] == 0 and temp:
            count += fight(A[i], temp, fishes)
	
    print("A", A, "fishes:", fishes, "temp", temp)
	
    return count + len(temp)
	

assert get_remaining_fish([1],[0]) == 1
assert get_remaining_fish([1,2],[0,1]) == 2
assert get_remaining_fish([1,2],[0,0]) == 2
assert get_remaining_fish([1,2,3],[0,0,0]) == 3
assert get_remaining_fish([0,1,2],[1,0,1]) == 2

assert get_remaining_fish([4,3,2,1,5],[0,1,0,0,0]) == 2
assert get_remaining_fish([4,3,2,1,5],[0,1,0,0,0]) == 2