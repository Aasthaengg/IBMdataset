n = int(input())
now, bef = 0, 0
ans = 0
for i in range(n):
  now = int(input())
  if now == 0 and bef == 1:
    bef = 0
  if (now+bef)%2 == 0:
    if bef == 0:
      ans += now//2
      bef = 0
    else:
      ans += (now+bef)//2
      bef = 0
  else:
    if bef == 0:
      ans += now//2
      bef = 1
    else:
      ans += (now+bef)//2
      bef = 1

print(ans)