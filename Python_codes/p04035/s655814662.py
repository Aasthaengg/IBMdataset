N,L = map(int, input().split())
A=list(map(int, input().split()))
choose = -1
for i in range(1, N):
    if A[i - 1] + A[i] >= L:
        choose = i - 1
        break
if choose == -1:
    print('Impossible')
else:
    print('Possible')
    for i in range(0, choose):
        print(i + 1)
    for i in range(N - 1, choose + 1, -1):
        print(i)
    print(choose + 1)