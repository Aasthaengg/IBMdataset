def slove():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    l = list(map(int, input().rstrip('\n').split()))
    l.sort()
    cnt = 0
    for i in range(0, n * 2, 2):
        cnt += min(l[i], l[i+1])
    print(cnt)


if __name__ == '__main__':
    slove()
