import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    ans = 0
    amari = 0
    for a in A:
        if amari == 0:
            amari = a % 2
            ans += a // 2
        else:
            ans += min(amari, a)
            a = max(0, a - amari)
            ans += a // 2
            amari = a % 2

    print(ans)

    
    
    

if __name__ == '__main__':
    main()

