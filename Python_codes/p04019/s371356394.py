s = input()
dirset = set()
for i in s:
  dirset.add(i)
if "N" in dirset and "S" in dirset:
  if ("E" in dirset and "W" in dirset) or (not "E" in dirset and not "W" in dirset):
    print("Yes")
  else:
    print("No")
elif "E" in dirset and "W" in dirset:
  if not "N" in dirset and not "S" in dirset:
    print("Yes")
  else:
    print("No")
else:
  print("No")