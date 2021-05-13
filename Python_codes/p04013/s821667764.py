
N,A = map(int,input().split())

lis = []

for i in range(51):
    lis.append([0] * 2501)

lis[0][0] = 1

X = list(map(int,input().split()))


for x in X:

    nlis = []
    for k in range(51):
        new = lis[k].copy()
        nlis.append(new)

    for i in range(51):

        for j in range(2501):

            if i+1 <= 50 and j+x <= 2500 and nlis[i][j] > 0:

                lis[i+1][j+x] += nlis[i][j]

ans = 0
for i in range(51):

    for j in range(2501):

        if i != 0 and j % i == 0 and j // i == A:
            #print (i,j,lis[i][j])
            ans += lis[i][j]

print (ans)
