t = input()
n = t.count('N')
s = t.count('S')
w = t.count('W')
e = t.count('E')

if (n>0 and s>0 and w>0 and e>0)or(n==0 and s==0 and w>0 and e>0) or (n>0 and s>0 and w==0 and e==0):
    print('Yes')
else:
    print('No')
