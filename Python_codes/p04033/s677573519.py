a, b = map(int, input().split())
if a > 0 and b > 0: ans = "Positive"
elif a < 0 and b < 0:
  if (abs(a-b) + 1) % 2 == 0:
    ans = "Positive"
  else:
    ans = "Negative"
else:
  ans = "Zero"
print(ans)