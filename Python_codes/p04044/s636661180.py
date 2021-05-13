def LI():
    return list(map(int, input().split()))


def LSH(h):
    return [input() for _ in range(h)]


N, L = LI()
S = LSH(N)
S.sort()
S = ''.join(S)
print(S)
