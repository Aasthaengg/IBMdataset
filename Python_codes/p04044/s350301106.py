N,L = map(int,input().split())
A = []

for i in range(N):
  s = input()
  A.append(s)
A.sort()
print("".join(A))