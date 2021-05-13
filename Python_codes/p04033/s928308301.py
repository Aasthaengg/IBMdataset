a, b = map(int, input().split())
if (0 < a):
  res = "Positive"

elif (a * b == 0) or (a * b < 0):
  res = "Zero"

else:
  if a == b:
    res = "Positive"
  elif (b-a) % 2 == 1:
    res = "Positive"
  else:
    res = "Negative"
print(res)