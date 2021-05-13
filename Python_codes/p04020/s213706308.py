#B
n = int(input())
cnt = 0
merge = 0
for _ in range(n):
    v = int(input())
    if v==0:
        merge = 0
    else:
        q,r = divmod(v,2)
        cnt += q
        cnt += (merge * r)
        merge = (1-merge)*r + (1-r)*merge
print(cnt)