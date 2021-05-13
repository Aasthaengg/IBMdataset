import sys
input = sys.stdin.readline

N, L = map(int, input().split())
a = list(map(int, input().split()))
for i in range(N-1):
    if a[i] + a[i+1] >= L:
        print('Possible')
        for j in range(1, i+1):
            print(j)
        for j in range(i+1, N)[::-1]:
            print(j)
        exit()
print('Impossible')