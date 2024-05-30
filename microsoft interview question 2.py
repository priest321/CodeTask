"""
2. Regular Expression Matching

Given an input string ( s ) and a pattern ( p ), implement regular expression matching with support for `'.'` and `'*'` where:
- `'.'` Matches any single character.
- `'*'` Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

### Example 1:
**Input:** s = "aa", p = "a"  
**Output:** false  
**Explanation:** "a" does not match the entire string "aa".

### Example 2:
**Input:** s = "aa", p = "a*"  
**Output:** true  
**Explanation:** '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

### Example 3:
**Input:** s = "ab", p = ".*"  
**Output:** true  
**Explanation:** ".*" means "zero or more (*) of any character (.)".

### Constraints:
- 1 ≤ s.length ≤ 20
- 1 ≤ p.length ≤ 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

def valid_re_exp(data: str, validition: str):
    re = [".", "*"]
    skip = False
    data = list(data)
    
    def get_value_index(value, v):
        data = [i for i in range(len(value)) if value[i] == v]
        return data[-1]+1
        
    for v in validition:
        if v not in re:
            if skip and v in data:
                index = get_value_index(data, v)
                data = data[index:]
                skip = False
            elif data[0] == v:
                del data[0]
            else:
                return False
                
        elif v == ".":
            del data[0]
            
        elif v == "*":
            skip = True
            
    if skip:
        data = []
    
    return True if not data else False
    
            
            
        


assert valid_re_exp("aa", "a*") == True
assert valid_re_exp("aa", "a.") == True
assert valid_re_exp("aa", "a") == False
assert valid_re_exp("ab", ".b") == True
assert valid_re_exp("abbbbbbc", "a*c") == True
assert valid_re_exp("abbbbbbc", "a..*c") == True
assert valid_re_exp("abcbbbbc", "a*b") == False
assert valid_re_exp("abcbbbbcb", "a*b") == True
assert valid_re_exp("abcbbbbcbe", "a*be") == True
assert valid_re_exp("abcbbbbcbeeebef", "a*b*f") == True



