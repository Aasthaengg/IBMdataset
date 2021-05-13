N,L = map(int,input().split())
A = list(map(int,input().split()))

last = -1
for i,(a,b) in enumerate(zip(A,A[1:])):
    if a+b >= L:
        last = i
        break
if last < 0:
    print('Impossible')
    exit()
print('Possible')

ans = list(range(1,i+1)) + list(range(N-1,i,-1))
print(*ans, sep='\n')