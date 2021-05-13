S = input()
if "S" in S and "N" not in S:
  print("No")
elif "N" in S and "S" not in S:
  print("No")
elif "E" in S and "W" not in S:
  print("No")
elif "W" in S and "E" not in S:
  print("No")
else:
  print("Yes")