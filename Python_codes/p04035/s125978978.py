N,L = map(int,input().split())
A = list(map(int,input().split()))

for i,(a,b) in enumerate(zip(A,A[1:])):
    if a+b >= L:
        print('Possible')
        break
else:
    print('Impossible')
    exit()
ans = []
for j in range(1,i+1):
    ans.append(j)
for j in range(N-1,i+1,-1):
    ans.append(j)
ans.append(i+1)
print(*ans, sep='\n')