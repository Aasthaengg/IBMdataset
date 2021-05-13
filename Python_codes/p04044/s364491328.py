N, L = list(map(lambda a: int(a), input().split(" ")))
A = []
for i in range(N):
  A.append(input())
  
A.sort()
print("".join(A))