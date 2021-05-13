s = input()
ans = ""
for i in range(len(s)):
  if s[i] == "0":
    ans += "0"
  elif s[i] == "1":
    ans += "1"
  else:
    if len(ans) >= 1:
      ans = ans[:-1]
print(ans)