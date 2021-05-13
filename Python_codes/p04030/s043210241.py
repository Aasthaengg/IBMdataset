s = input()

lis = []
for k in s:
  if k == "B":
    if len(lis) != 0:
      lis.pop()
  else:
    lis.append(k)

print("".join(lis))
