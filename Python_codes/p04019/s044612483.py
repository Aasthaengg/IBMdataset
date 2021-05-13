S = input()

n = 0
e = 0
w = 0
s = 0

for v in S:
    if v == 'N': n+=1
    if v == 'E': e+=1
    if v == 'W': w+=1
    if v == 'S': s+=1
if ((0<n and 0<s) or (n==0 and s==0)) and ((0<e and 0<w) or (e==0 and w==0)):
    print('Yes')
else:
    print('No')