def main():
    import sys
    input = sys.stdin.readline
    N, M = [int(x) for x in input().strip().split()]
    f = [False] * N
    c = [1] * N
    f[0] = True
    
    for m in range(M):
        x, y = [int(x) for x in input().strip().split()]
        f[y-1] = f[y-1] or f[x-1]
        c[y-1] += 1
        c[x-1] -= 1
        if c[x-1] == 0:
            f[x-1] = False
        
    print(len([1 for b in f if b]))

if __name__ == '__main__':
    main()