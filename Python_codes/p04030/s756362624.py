s = input()
num = len(s)
ans = ""

for i in range(num):
  if s[i] != 'B':
    ans += s[i]
  elif len(ans) != 0:
    ans = ans[:-1]

    
print(ans)