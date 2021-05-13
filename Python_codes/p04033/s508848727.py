a,b=map(int,input().split())
ans=""
if a<=0<=b:
    ans="Zero"
elif (a<=b<0 and (b-a)%2==1) or 0<a<=b:
    ans="Positive"
else:
    ans="Negative"
print(ans)
