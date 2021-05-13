import collections

S = input()

c = collections.Counter(S)
K = c.keys()

if len(K) == 4:
    print('Yes')
elif len(K) == 2:
    if 'N' in K and 'S' in K:
        print('Yes')
    elif 'W' in K and 'E' in K:
        print('Yes')
    else:
        print('No')
else:
    print('No')