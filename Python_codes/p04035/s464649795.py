n,l = map(int, input().split())
As = list(map(int, input().split()))
# 和がl以上のものがあれば、それを残してあとを端から落としていくのでよい
ss = [As[i]+As[i+1] for i in range(n-1)]
# print(ss)
cnt = 0
for i,s in enumerate(ss):
    if s >= l:
        cnt = i + 1
if cnt == 0:
    print("Impossible")
    exit()
print("Possible")
for i in range(1,cnt):
    print(i)
for i in range(n-1, cnt, -1):
    print(i)
print(cnt)