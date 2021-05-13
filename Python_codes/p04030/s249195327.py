def bs(s):
  if s == "":
    return s
  else:
    return s[:-1]
 
s = input()
ans = ""
for c in s:
  if c == "B":
    ans = bs(ans)
  else:
    ans += c
print(ans)