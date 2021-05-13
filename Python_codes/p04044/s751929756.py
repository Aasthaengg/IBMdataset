def solve():
    N, L = [int(i) for i in input().split()]
    S = []
    for _ in range(N):
        S.append(input())
    print(''.join(sorted(S)))

if __name__ == "__main__":
    solve()