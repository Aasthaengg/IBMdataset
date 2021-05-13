s = input()
ans = list()
for ss in s:
  if ss == '0':
    ans.append('0')
  elif ss == '1':
    ans.append('1')
  else:
    if ans:
      ans.pop(-1)

print(''.join(ans))