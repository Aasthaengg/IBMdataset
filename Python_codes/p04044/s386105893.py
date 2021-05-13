N, L = map(int, input().split())

S = [input() for _ in range(N)]

S.sort()

res = "".join(S)

print(res)