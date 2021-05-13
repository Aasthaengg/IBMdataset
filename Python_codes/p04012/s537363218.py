w = input()
dict = {}
for i in w:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] +=1
for key, value in dict.items():
  if value % 2 != 0:
    print("No")
    exit()
print("Yes")