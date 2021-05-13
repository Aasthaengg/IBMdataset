N, L = map(int, input().split())
S = [input() for s in range(N)]
S.sort()
output = ""
for i in S:
  output+=i
print(output)