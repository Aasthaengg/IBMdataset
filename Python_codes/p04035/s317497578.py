N,L = map(int,input().split())
src = list(map(int,input().split()))

for i,(a,b) in enumerate(zip(src, src[1:])):
    if a+b >= L:
        print('Possible')
        for j in range(1,i+1): print(j)
        for j in range(N-1,i,-1): print(j)
        exit()
print('Impossible')
