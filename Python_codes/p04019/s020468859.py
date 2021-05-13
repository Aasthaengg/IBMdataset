S = input()
n, w = S.count('N'), S.count('W')
s, e = S.count('S'), S.count('E')
flag = True
if n == 0 or s == 0:
    if n != s:
        flag = False
if w == 0 or e == 0:
    if w != e:
        flag = False
print('Yes' if flag else 'No')
