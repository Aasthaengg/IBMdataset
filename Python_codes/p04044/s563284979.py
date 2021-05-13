n,l=map(int, input().split(' '))

ss= []
for i in range(n):
  ss.append(input())
ss.sort()

ans= ''
for i in ss:
  ans+=i
  
print(ans)