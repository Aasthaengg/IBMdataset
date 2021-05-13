s = list(input())
box = []
for i in range(len(s)):
  if s[i] == "0":
    box.append("0")
  elif s[i] == "1":
    box.append("1")
  else:
    if box == []:
      pass
    else:
      box.pop(-1)
print("".join(box))