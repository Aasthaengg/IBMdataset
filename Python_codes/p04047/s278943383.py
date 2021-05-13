def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse = True)
    ans = 0
    for i in range(N):
        ans += L[2*i+1]
    return ans

if __name__ == '__main__':
    print(main())