S = input()
ans = True
if ('S' in S) ^ ('N' in S):
    ans = False
if ('W' in S) ^ ('E' in S):
    ans = False
if ans:
    print('Yes')
else:
    print('No')
