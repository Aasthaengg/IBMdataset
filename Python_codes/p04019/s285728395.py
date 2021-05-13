U=list(str(input()))
if "N" in U:
  if "S" not in U:
    print("No")
    exit()
if "S" in U:
  if "N" not in U:
    print("No")
    exit()
if "E" in U:
  if "W" not in U:
    print("No")
    exit()
if "W" in U:
  if "E" not in U:
    print("No")
    exit()
print("Yes")