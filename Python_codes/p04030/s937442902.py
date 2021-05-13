s = ""
for i in (input()):
  if i in ["0", "1"]:
    s = s + i
  else:
    if len(s) >0:
    	s = s[:-1]

print(s)