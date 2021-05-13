a,b,c = map(int,input().split())
A = [a,b,c]
B = [a,b,c]
A = A.count(5)
B = B.count(7)
if A == 2 and B == 1:
  print("YES")
else:
  print("NO")