n,l = map(int,input().split())
s_list = []
for i in range(n):
    s_list.append(str(input()))
s_sort = sorted(s_list)
ans = ''
for i in range(n):
    ans += s_sort[i]
print(ans)
