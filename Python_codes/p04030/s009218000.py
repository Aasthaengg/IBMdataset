s = list(input())

ans = []
for t in s:
  if t == "0":
    ans.append("0")
  elif t == "1":
    ans.append("1")
  elif t == "B" and ans != []:
    ans.pop(-1)
print("".join(ans))