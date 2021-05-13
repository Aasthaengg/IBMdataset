N = int(input())
A = list(map(int, input().split()))

A.sort()
A = A[::2]
print(sum(A))