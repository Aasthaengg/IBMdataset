import sys
input = sys.stdin.readline

def main():
    N = int(input())
    l = sorted(list(map(int, input().split())), reverse=True)

    ans = 0
    for i in range(0, N*2, 2):
        ans += min(l[i], l[i+1])
    print(ans)


if __name__ == "__main__":
    main()