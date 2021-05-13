s = set(list(input()))

if 'N' in s:
  if not 'S' in s:
    print("No")
    exit()
  elif len(s) == 2 or len(s)==4:
    print("Yes")
    exit()
    
if 'S' in s:
  if not 'N' in s:
    print("No")
    exit()
  elif len(s) == 2 or len(s)==4:
    print("Yes")
    exit()

if 'W' in s:
  if not 'E' in s:
    print("No")
    exit()
  elif len(s) == 2 or len(s)==4:
    print("Yes")
    exit()

if 'E' in s:
  if not 'W' in s:
    print("No")
    exit()
  elif len(s) == 2 or len(s)==4:
    print("Yes")
    exit()
    
print("No")