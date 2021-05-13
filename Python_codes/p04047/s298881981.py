n=int(input())
x=input().split()
l=[]
for k in range(2*n):
  l.append(int(x[k]))
l.sort()
s=0
for k in range(2*n):
  if k%2==0:
    s+=l[k]
print(s)   