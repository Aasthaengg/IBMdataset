N = int(input())
A = list(map(int, input().split()))
A.sort()
print(sum(A[2*i] for i in range(N)))