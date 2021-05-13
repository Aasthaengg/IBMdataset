S = str(input())
n = S.count('N')
w = S.count('W')
s = S.count('S')
e = S.count('E')
if (n == 0 and 0 < s) or (s == 0 and 0 < n) or (e == 0 and 0 < w) or (w == 0 and 0 < e):
    print('No')
else:
    print('Yes')