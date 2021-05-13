#A - Wanna go back home
S = list(input())

N = S.count('N')
E = S.count('E')
W = S.count('W')
s = S.count('S')

if ((N>0 and s>0) and ((E>0 and W>0) or (E == W == 0))) or ((N == s == 0) and ((E>0 and W>0) or (E == W == 0))):
    print('Yes')
else:
    print('No')