
n,l=map(int,input().split())
str=[input() for i in range(n)]
str.sort()
ans=""
for i in range(n):
    ans+=str[i]
print(ans)