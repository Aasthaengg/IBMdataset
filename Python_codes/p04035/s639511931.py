def solve():
    global N, L
    N, L = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(N-1):
        if a[i]+a[i+1]>=L:
            return i+1
    return False
ans = solve()
if ans:
    print('Possible')
    for i in range(1, ans):
        print(i)
    for i in range(N-1, ans, -1):
        print(i)
    print(ans)
else:
    print("Impossible")