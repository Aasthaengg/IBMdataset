n=input()
ans1, ans2="No", "No"
ans3, ans4="No", "No"
if 'N' in n:
  if 'S' in n:
    ans1="Yes"
if 'S' in n:
  if 'N' in n:
    ans2="Yes"
if 'E' in n:
  if 'W' in n:
    ans3="Yes"
if 'W' in n:
  if 'E' in n:
    ans4="Yes"
if "W" not in n and "E" not in n:
    ans3, ans4 = "Yes", "Yes"
if "N" not in n and "S" not in n:
    ans1, ans2 = "Yes", "Yes"
if ans1=="Yes" and ans2=="Yes" and ans3=="Yes" and ans4=="Yes":
  print("Yes")
else:
  print("No")