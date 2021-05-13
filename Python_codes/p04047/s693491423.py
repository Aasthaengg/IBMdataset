N = int(input())
A = sorted([int(a) for a in input().split()])
print(sum(A[::2]))