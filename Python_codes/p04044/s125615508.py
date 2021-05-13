H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

S.sort()
#print(S)
S_out=''
for ii in S:
  S_out += ii
print(S_out)
