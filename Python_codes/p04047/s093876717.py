#AGC001A
N = int(input())
Ls = list(map(int, input().split()))

Ls.sort(reverse=True)
res = sum(Ls[1::2])

print(res)