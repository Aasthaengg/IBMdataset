l = list(input())
n = l.count('N')
w = l.count('W')
s = l.count('S')
e = l.count('E')
if n == s or (n != 0 and s != 0):
    if w == e or (w != 0 and e != 0):
        print('Yes')
        exit(0)
print('No')