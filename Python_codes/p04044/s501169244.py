# 入力
N,L = list(map(int, input().split()))
S = []
for _ in range(N):
    S += [str(input())]

# 出力
print(''.join(sorted(S)))