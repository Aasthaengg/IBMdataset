n=int(input())
integers=list(map(int,input().split()))
 
sql=[x**2 for x in integers]
s=sum(integers)
t=sum(sql)
m=min(s%n, n-s%n)
 
print((m**2-s**2)//n+t)