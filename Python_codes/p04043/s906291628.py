A,B,C=map(int,input().split())
n5=0
n7=0
if A==7:
  n7 += 1
elif A==5:
  n5 += 1
if B==7:
  n7 += 1
elif B==5:
  n5 += 1
if C==7:
  n7 += 1
elif C==5:
  n5 += 1

if n5==2 and n7==1:
  print("YES")
else:
  print("NO")