s = input()
ans =[]
for i in s:
  if i == "B":
    if ans ==[]:
      continue
    else:
      del ans[-1]
  else:
    ans += i
print("".join(ans))