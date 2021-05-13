n = input()
l = list(map(int, input().split()))
l.sort(reverse=True)
c = 0
ans = 0
for i in l: 
    if c % 2 == 1:
        ans+=l[c]
    c+=1
print(ans)