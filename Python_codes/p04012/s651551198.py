s = input()
d = {}

for letter in s:
  if letter in d:
    d[letter] += 1
  else:
    d[letter] = 1
flag = 1  
for key in d:
  if d[key]%2 != 0:
    flag = 0
	
if flag == 1:
  print("Yes")
else:
  print("No")