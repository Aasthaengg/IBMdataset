n=int(input())
a=list(map(int,input().split()))
mins=100**2*n
for i in range(min(a),max(a)+1):
  sum=0
  for j in range(n):
    sum+=abs(a[j]-i)**2
  if sum<mins:
    mins=sum
print(mins)