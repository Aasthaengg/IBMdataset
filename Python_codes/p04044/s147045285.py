a,b=map(int,input().split())
c=[]

for i in range(a):
  c.append(input())

d=sorted(c)  
print(''.join(d))