S=input()
ans = []
for i in range(len(S)):
  if S[i] == "B":
    if len(ans) != 0:
      del ans[len(ans)-1]
  else:
    ans.append(S[i])
print("".join(map(str,ans)))