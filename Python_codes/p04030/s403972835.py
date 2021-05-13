S = list(input())
ans_list = []
for i in S:
  if i == "0":
    ans_list.append("0")
  elif i == "1":
    ans_list.append("1")
  else:
    if len(ans_list) != 0:
      del ans_list[-1]
ans = "".join(ans_list)    
print(ans)