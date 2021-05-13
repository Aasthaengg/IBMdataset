S = list(set(list(input())))
S.sort()
ans = "No"
if S[0] == 'E':
  if S[-1] == 'W':
    if len(S)==2 or len(S)==4:
      ans = "Yes"
if S[0] == 'N':
  if S[-1] == 'S':
    ans = "Yes"
print(ans)