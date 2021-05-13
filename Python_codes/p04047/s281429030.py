N = int(input())
A = sorted(map(int,input().split()),reverse=True)
C = []
for i in range(N):
  C.append(A[2*i + 1])
print(sum(C))