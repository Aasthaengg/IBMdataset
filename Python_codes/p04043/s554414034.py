A, B, C = map(int, input().split())

count_5 = 0
count_7 = 0

if A == 5:
  count_5 += 1
elif A == 7:
  count_7 += 1
  
if B == 5:
  count_5 += 1
elif B == 7:
  count_7 += 1
  
if C == 5:
  count_5 += 1
elif C == 7:
  count_7 += 1
  
if count_5 == 2 and count_7 == 1:
  print("YES")
else:
  print("NO") 
 
