a,b = map(int,input().split())

if a > 0:
  ans  = "Positive"
elif a == 0:
  ans = "Zero"
elif b >= 0:
  ans = "Zero"
else:
  if abs(a-b)%2 == 0:
    ans = "Negative"
  else:
    ans = "Positive"
print(ans)