if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))

    ans = (50*100)*(50*100)
    for i in range(-100,101):
        mn = 0
        for c in lst:
            mn += (i-c)*(i-c)
        ans = min(ans,mn)

    print(ans)
