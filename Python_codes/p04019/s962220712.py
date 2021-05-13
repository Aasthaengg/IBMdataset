S = input()

n = S.count('N')
s = S.count('S')
w = S.count('W')
e = S.count('E')

if n * s > 0 and w * e > 0:
    print('Yes')
elif n * s > 0 and w == 0 and e == 0:
    print('Yes')
elif w * e > 0 and n == 0 and s == 0:
    print('Yes')
else:
    print('No')
