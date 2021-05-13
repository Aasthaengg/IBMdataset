N=int(input())
A=[int(x) for x in input().split()]
A.sort()
print(sum([A[i] for i in range(len(A)) if i%2==0]))