N,L = map(int,input().split())
a = list(map(int,input().split()))
x = N
for i in range(1,N):
    if a[i] + a[i-1] >= L:
        x = i
if x == N:
    print('Impossible')
    exit()
print('Possible')
for i in range(1,x):
    print(i)
for i in range(N-1,x-1,-1):
    print(i)
