a, b = map(int, input().split())
if a*b <= 0:
  ans = 'Zero'
elif a>0:
  ans = 'Positive'
elif (b-a+1)%2 == 0:
  ans = 'Positive'
else:
  ans = 'Negative'
  
print(ans)