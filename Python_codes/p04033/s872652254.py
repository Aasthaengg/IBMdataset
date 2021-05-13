a, b=map(int, input().split())
ans=''

if a<=0 and b>=0:
  ans='Zero'
elif b<0:
  if (b-a+1)%2==0:
    ans='Positive'
  else:
    ans='Negative'
else:
  ans='Positive'
print(ans)