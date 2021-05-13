a,b,c = map(str, input().split())
ok = ["575", "557", "755"]
if (a+b+c in ok):
  print("YES")
else:
  print("NO")