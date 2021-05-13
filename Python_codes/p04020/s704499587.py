n = int(input())
ans = 0
li = []
tmp = 0
for i in range(n):
    t = int(input())
    if t == 0:
        li.append(tmp)
        tmp = 0
    else:
        tmp += t
li.append(tmp)
for l in li:
    ans += l//2
#print(li)
print(ans)