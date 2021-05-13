#002_C
n, l = map(int, input().split())
a = list(map(int, input().split()))

flg = False
ans = []
for i in range(n-1):
    if a[i] + a[i+1] >= l:
        ans = [j for j in range(1, i+1)] + [j for j in range(n-1, i+1, -1)] + [i+1]
        flg = True
        break
    
if flg:
    print('Possible')
    print(*ans, sep='\n')
else:
    print('Impossible')