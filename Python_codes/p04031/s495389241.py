from math import ceil,floor
ansc,ansf = 0,0
n = int(input())
a = list(map(int,input().split()))
 
gp = sum(a)/len(a)
c = ceil(gp)
f = floor(gp)

for i in a:
  ansc += (i-c)**2
  ansf += (i-f)**2
  
print(min(ansc,ansf))