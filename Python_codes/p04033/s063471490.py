a,b = map(int,input().split())

if((a<=0)and(0<=b)):
  ans = 'Zero'
elif((a>=0)and(b>=0)):
  ans = 'Positive'
elif((a<0)and(b<0)):
  if((b-a)%2 == 1):
    ans = 'Positive'
  else:
    ans = 'Negative'
print(ans)   