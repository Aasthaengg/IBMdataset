a,b,c = map(int,input().split())

if a == 7:
  if b == 5 and c == 5:
    print("YES")
  else:
    print("NO")
elif b == 7:
  if a == 5 and c == 5:
    print("YES")
  else:
    print("NO")
elif c == 7:
  if a == 5 and b == 5:
    print("YES")
  else:
    print("NO")
else:
  print("NO")