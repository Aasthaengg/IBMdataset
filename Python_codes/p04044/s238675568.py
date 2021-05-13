n,l=map(int,input().split())
s=[]
for i in range(n):
  x=input()
  s.append(x)

s.sort()
a=""
for i in range(n):
  a+=s[i]

print(a)