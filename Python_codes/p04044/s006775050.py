N, L = map(int, input().split())
S = [str(input()) for i in range(N)]

S = sorted(S)


print(''.join(S))