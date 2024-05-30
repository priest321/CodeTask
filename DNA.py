"""
Find minimal nucleotide of DNA
_____________________
example:



"""

def get_affect(data: str, start: list, end: list):
    dna = [("A", 1), ("C", 2), ("G", 3), ("T", 4)]
    output = []
    def get_value(partial_data):
        for k, v in dna:
            if k in partial_data:
                output.append(v)
                break

    for i in range(len(start)):
        partial_data = data[start[i]:end[i]+1]
        get_value(partial_data)
    
    return output

assert get_affect('CAGCCTA', [2, 5, 0], [4, 5, 6]) == [2,4,1]

