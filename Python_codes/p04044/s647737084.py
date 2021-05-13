N, L = map(int, input().split())
s = []
for i in range(N):
  s.append(input())
  
s = sorted(s)

print("".join(s))