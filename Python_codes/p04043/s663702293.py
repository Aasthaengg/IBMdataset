A, B, C = map(int, input().split())
L = [A, B, C]
ans = [[5, 5, 7], [5, 7, 5], [7, 5, 5]]

if L in ans:
  print("YES")
else:
  print("NO")