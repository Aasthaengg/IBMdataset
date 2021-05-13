
def solve():
    N, M = map(int, input().split())
    exist = [1] * N
    red = [False] * N
    red[0] = True
    for i in range(M):
        x, y = map(int, input().split())
        x -= 1; y -= 1
        exist[x] -= 1; exist[y] += 1
        if red[x]:
            red[y] = True
        if exist[x] == 0:
            red[x] = False
    ans = 0
    for i in range(N):
        if red[i] and exist[i] > 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()