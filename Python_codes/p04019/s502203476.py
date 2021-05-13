s = input()
if "N" in s:
  if "S" not in s :
    print("No")
    exit()
if "E" in s:
  if "W" not in s:
    print("No")
    exit()
if "S" in s:
  if "N" not in s :
    print("No")
    exit()
if "W" in s:
  if "E" not in s:
    print("No")
    exit()
print("Yes")