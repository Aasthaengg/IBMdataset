S=list(input())
if ('N' in S and 'S' not in S) or ('S' in S and 'N' not in S) or ('W' in S and 'E' not in S) or ('E' in S and 'W' not in S):
    print('No') 
else:
    print('Yes')