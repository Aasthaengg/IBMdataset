def resolve():
    N, L = list(map(int, input().split()))
    S_list = [input() for i in range(N)]
    print("".join(sorted(S_list)))

resolve()