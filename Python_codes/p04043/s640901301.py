A,B,C = map(int,input().split())
res = "NO"
if A == 5 or A == 7:
  if B == 5 or B == 7:
    if C == 5 or C == 7:
      if A+B+C == 17:
        res = "YES"
print(res)