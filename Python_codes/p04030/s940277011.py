import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    s = readline().strip()

    ans = []
    for c in s:
        if c in ('0', '1'):
            ans.append(c)
        elif ans:
            ans.pop()

    print(''.join(ans))
    return


if __name__ == '__main__':
    main()
