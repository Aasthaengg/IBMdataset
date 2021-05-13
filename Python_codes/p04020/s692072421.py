def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    ans = 0
    p = 0
    for n in range(N):
        a = int(input())
        ans += min(p, a)
        p = max(0, a - p)
        ans += p // 2
        p %= 2
    print(ans)
    
if __name__ == '__main__':
    main()