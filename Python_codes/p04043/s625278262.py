A, B, C = map(int, input().split())
if min(A, B, C) == 5 and max(A, B, C) == 7 and A + B + C == 17:
  print("YES")
else:
  print("NO")