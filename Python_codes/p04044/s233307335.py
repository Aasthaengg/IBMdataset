def resolve():
    N, L = map(int, input().split())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    S = sorted(S)
    ans = ""
    for i in range(N):
        ans += S[i]
    print(ans)
resolve()