A,B,C = map(int,input().split())
b_5 = 0
b_7 = 0
if A == 5:
  b_5 += 1
elif A == 7:
  b_7 += 1
if B == 5:
  b_5 +=1
elif B==7:
  b_7 += 1
if C==5:
  b_5 +=1
elif C==7:
  b_7 += 1

if b_5 == 2 and b_7 == 1:
  print("YES")
else:
  print("NO")