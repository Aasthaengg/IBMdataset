N=int(input())
L=[int(i) for i in input().split()]
L.sort()
K=[]
for i in range(N):
    K.append(L[i*2])

print(sum(K))


