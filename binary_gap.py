"""
get binary gap:
example 
_____________________
<input> is a int between 1 - 100 milion
1001 got gap of 2 should return 2
10100 should return 1
111111 should return 0
100001001 should return 5
"""

def get_binary_gap(N):
    binary_data = format(N, 'b')
    gap = 0
    step = 0
    for i in binary_data:
        if i == "1":
            gap = step if gap < step else gap
            step = 0
        elif i == "0":
            step += 1
            
    return gap

assert get_binary_gap(-4) == 0 # -100
assert get_binary_gap(0) == 0 # 0 
assert get_binary_gap(9) == 2 # 1001
assert get_binary_gap(15) == 0 # 1111
assert get_binary_gap(199) == 3 # 11000111
assert get_binary_gap(199999) == 4 # 110000110100111111
assert get_binary_gap(561892) == 3 # 10001001001011100100
