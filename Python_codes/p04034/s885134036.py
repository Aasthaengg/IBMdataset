n,m = map(int,input().split())

in_group = set()
in_group.add(1)

boll_num = {}
for i in range(n):
    boll_num[i+1] = 1


for i in range(m):
    x,y = map(int,input().split())
    if(x in in_group):
        in_group.add(y)
        if(boll_num[x] == 1):
            in_group.remove(x)
    
    boll_num[x] = boll_num.setdefault(x,0) - 1
    boll_num[y] = boll_num.setdefault(y,0) + 1

print(len(in_group))
