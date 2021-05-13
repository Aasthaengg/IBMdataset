def MAP(): return map(int, input().split())
a, b, c = sorted(MAP())
if a == 5 and b == 5 and c == 7:
  print("YES")
else:
  print("NO")