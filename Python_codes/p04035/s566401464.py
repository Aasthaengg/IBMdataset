# 隣り合う和がL未満ならそもそもimpossible
# ならば隣り合う和がL以上ならば？ -> そこから連続して隣り合うやつをどうやって足しても常にL以上

n, l = map(int, input().split())
a = list(map(int, input().split()))
idx = 0
for i in range(1, n):
    if a[i - 1] + a[i] >= l:
        idx = i
        break
if idx == 0:
    print("Impossible")
    exit()

print("Possible")

ans = [idx]
for i in range(idx - 1, 0, -1):
    ans.append(i)
for i in range(idx + 1, n):
    ans.append(i)
for a in ans[::-1]:
    print(a)