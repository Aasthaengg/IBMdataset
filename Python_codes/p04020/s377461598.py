n = int(input())
ans = 0
flow = 0
for i in range(n):
  a = int(input())
  if a == 0:
    flow = 0
  else :
    ans += (a + flow) // 2
    flow = (a + flow) % 2
print(ans)