def f(n,x,i):
    if n == 0:
        if x != 0:
            if x / i == a:
                return 1
        return 0
    if memo[i][n][x] != -1:
        return memo[i][n][x]
    memo[i][n][x] = f(n-1,x,i)+f(n-1,x+ary[n-1],i+1)
    return memo[i][n][x]
n,a = map(int,input().split())
ary = list(map(int,input().split()))
memo = [[[-1 for _ in range(sum(ary)+1)] for _ in range(n+1)] for _ in range(n+1)]
print(f(n,0,0))