import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N-1):
    if A[i] + A[i+1] >= L:
        print("Possible")
        for j in range(1, i+1):
            print(j)
        for j in range(i+1, N)[::-1]:
            print(j)
        sys.exit()

print("Impossible")