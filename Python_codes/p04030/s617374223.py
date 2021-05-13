s = list(input())
n = len(s)

ans = []
for i in range(n):
  if s[i] == '0':
    ans.append('0')
  elif s[i] == '1':
    ans.append('1')
  elif ans == []:
    continue
  else:
    ans.pop()
    
print(''.join(ans))
    
