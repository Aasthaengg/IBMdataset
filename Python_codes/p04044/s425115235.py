n,l = map(int,input().split())
s = [input() for i in range(n)]
s.sort()
ans = ""
for i in s:
    ans = "".join([ans,i])
print(ans) 