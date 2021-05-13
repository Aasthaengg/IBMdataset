ai = lambda: list(map(int, input().split()))

n,l = ai()
a = ai()

f = 0
for i in range(1,n):
    if a[i-1]+a[i] >= l:
        f = 1
        key = i
        break
if f:
    print('Possible')
    b = list(range(n))
    c = b[1:key]
    c += b[-1:key:-1]
    c += [key]
    print(*c, sep='\n')
else:
    print('Impossible')
