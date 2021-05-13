def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = 0
    for a in A:
        ans += a//2
    prev = 0
    for a in A:
        new = a%2
        if prev == 1:
            if new == 1:
                ans += 1
            elif a>0:
                prev = 1
            else:
                prev = 0
        prev = prev^new
    return ans
print(solve())