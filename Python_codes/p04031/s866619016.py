import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = sum(A) // N
    ans = 10**10
    for x in range(c, c + 2):
        val = 0
        for a in A: val += (x - a) ** 2
        ans = min(ans, val)
    print(ans)

if __name__ == "__main__":
    main()
