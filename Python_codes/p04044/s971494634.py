import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    N, L = map(int, input().rstrip().split())
    s = []
    for _ in range(N):
        s.append(input().rstrip())
    ans = ''
    for st in sorted(s):
        ans += st
    print(ans)


if __name__ == '__main__':
    main()
