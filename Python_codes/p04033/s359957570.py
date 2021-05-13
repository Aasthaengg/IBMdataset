a,b=map(int,input().split())

if (a>0 and b<0) or (a<0 and b>0):
  ans="Zero"
elif a==0 or b==0:
  ans="Zero"
elif a>0 and b>0:
  ans="Positive"
elif a<0 and b<0:
  if (a%2==0 and b%2==0) or (a%2!=0 and b%2!=0):
    ans="Negative"
  else:
    ans="Positive"
    
print(ans)
