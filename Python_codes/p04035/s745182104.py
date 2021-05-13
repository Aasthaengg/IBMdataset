# coding: utf-8
N, L = map(int, input().split())
A = list(map(int, input().split()))
# Lより小さい組み合わせしか無い場合おわり
flag = False
for i in range(N-1):
    if A[i] + A[i+1] >= L:
        importance_i = i
        flag = True
        break
if not flag:
    print("Impossible")
    exit()

l, r = 0, N-1
print("Possible")
ans = []
while r - l > 1:
    # print(l, r)
    if l < importance_i:
        ans.append(l+1)
        l += 1
    if r > importance_i+1:
        ans.append(r)
        r -= 1
# print("importance_i", importance_i)
ans.append(importance_i+1)
print(*ans, sep="\n")