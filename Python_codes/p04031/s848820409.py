def solve():
    N = int(input())
    A = list(map(int,input().split()))

    ans = float('inf')
    for i in range(-100, 100+1):
        cnt = 0
        for a in A:
            cnt += (i-a) ** 2 
        ans = min(ans, cnt)
    
    print(ans)

if __name__ == '__main__':
    solve()