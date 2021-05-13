def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = 0
    for i in range(n-1):
        ans += a[i] // 2
        a[i] %= 2
        ans += min(a[i], a[i+1])
        a[i+1] -= min(a[i], a[i+1])
    ans += a[n-1] // 2
    print(ans)

if __name__ == "__main__":
    main()