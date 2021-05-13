def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    ans = 0
    for i in range(1, 2*n, 2):
        ans += l[i]
    print(ans)

if __name__ == "__main__":
    main()