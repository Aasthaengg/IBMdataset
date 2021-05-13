n, a = map(int,input().split())
X = list(map(int,input().split()))

X.sort()
ii = 0
while ii < n and X[ii] < a:
    ii += 1
jj = ii
while jj < n and X[jj] == a:
    jj += 1

aa = jj-ii
A = [[a-i for i in X[:ii]], [j-a for j in X[jj:]]]

# print(A)

mm = min(sum(A[0]), sum(A[1]))

AA = [[0] * (mm + 1) for i in range(2)]
for k in range(2):
    AA[k][0] = 1
    for i in range(len(A[k])):
        for j in range(len(AA[k])-1, -1, -1):
            if j - A[k][i] >= 0:
                AA[k][j] += AA[k][j-A[k][i]]
                # print(AA)
                # print(k, j, A[k][i])


# print(AA,aa)
ans = 0
for i in range(1, mm + 1):
    ans += AA[0][i] * AA[1][i]
# print(ans)
ans *= 2 ** aa

print(ans + (2 ** aa - 1))
            
