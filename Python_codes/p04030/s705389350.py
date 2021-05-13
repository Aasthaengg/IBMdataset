def solve():
  S = input()
  ans = []
  for s in S:
    if s!='B':
      ans.append(s)
    else:
      if len(ans):
        ans.pop(-1)
  ans = ''.join(ans)
  return ans
print(solve())