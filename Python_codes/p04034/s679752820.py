n, m = map(int,input().split())
all_li = []
for _ in range(m):
    li = list(map(int,input().split()))
    all_li.append(li)
#print(all_li)
flag_memo = [False]*n
flag_memo[0] = True
#print(flag_memo)
kazu_li = [1]*n
#print(kazu_li)

for a in all_li:
    kazu_li[a[0]-1] -= 1
    kazu_li[a[1]-1] += 1
    if flag_memo[a[0]-1]:
        flag_memo[a[1]-1] = True
    if kazu_li[a[0]-1] == 0:
        flag_memo[a[0]-1] = False
print(flag_memo.count(True))