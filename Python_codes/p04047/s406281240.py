n=int(input())
x=sorted(list(map(int,input().split())))
s=0
for i in range(n):
  s+=x[i*2]
print(s)