N, L = map(int, input().split())
A = list(map(int, input().split()))
flg = False
for i in range(N - 1):
    if A[i] + A[i+1] >= L:
        flg = True
        break
if not flg:
    print("Impossible")
    exit()
else:
    print("Possible")
# 0, 1, ..., i - 1, [i], [i+1], i + 2, ..., N - 1
for j in range(i):
    print(j + 1)
for j in range(N - 1, i + 1, -1):
    print(j)
print(i + 1)
