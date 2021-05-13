S = input()
ans = ""
flag = 0
for s in S[::-1]:
  if s == "B":
    flag += 1
    continue
  if flag:
    flag -= 1
    continue
  ans += s
print(ans[::-1])