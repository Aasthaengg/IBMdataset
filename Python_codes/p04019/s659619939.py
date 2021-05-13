s=str(input())
s=list(s)
if "W" in s and "E" not in s:
  print("No")
elif "E" in s and "W" not in s:
  print("No")
elif "N" in s and "S" not in s:
  print("No")
elif "S" in s and "N" not in s:
  print("No")
else:
  print("Yes")