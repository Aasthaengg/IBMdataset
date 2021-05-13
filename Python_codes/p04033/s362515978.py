def solve(a,b):
  if a <= 0 and b >= 0:
    return "Zero"
  elif a < b < 0 and (b-a+1) % 2 == 1:
    return "Negative"
  else:
    return "Positive"
    

a,b = map(int,input().split())
print(solve(a,b))