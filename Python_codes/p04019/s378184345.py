s = list(input())
we = [0,0]
ns = [0,0]

for i in range(len(s)):
    if s[i] == ('N'):
        ns[0] = 1
    elif s[i] == ('W'):
        we[0] = 1
    elif s[i] == ('S'):
        ns[1] = 1
    else:
        we[1] = 1

if sum(we) % 2 == 0 and sum(ns) % 2 == 0:
    print('Yes')
else:
    print('No')