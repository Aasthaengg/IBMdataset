S=[x for x in input()]
ans=[]
for i in range(len(S)):
  if S[i]!='B':
    ans.append(S[i])
  else:
    try:
      ans.pop()
    except:
      continue
print(''.join(ans))