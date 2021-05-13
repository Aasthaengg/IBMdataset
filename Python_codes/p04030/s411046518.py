x = str(input())
lst = []

for i in range(len(x)):
  if x[i] == 'B':  
    if len(lst) >0:
      lst.pop()
  else:
    lst.append(x[i])
print("".join(lst))