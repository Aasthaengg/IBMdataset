N, L = map(int, input().split())
s = [str(input()) for i in range(N)]
s.sort()
S=""
for i in range(N):
    S+=s[i]
print(S)