N, L = map(int, input().split())
A = [int(i) for i in input().split()]

for i in range(1, N):
    if A[i-1]+A[i] >= L:
        print('Possible')
        ans = []
        for j in range(1, i):
            ans.append(j)
        for k in range(N-1, i, -1):
            ans.append(k)
        ans.append(i)
        print(*ans, sep='\n')
        exit()
print('Impossible')
