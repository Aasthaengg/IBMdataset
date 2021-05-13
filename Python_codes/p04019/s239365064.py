S = list(input())
if 'N' in S and 'W' in S and 'S' in S and 'E' in S:
    print('Yes')
elif 'N' in S and 'S' in S and 'W' not in S and 'E' not in S:
    print('Yes')
elif 'N' not in S and 'S' not in S and 'W' in S and 'E' in S:
    print('Yes')
else:
    print('No')