NN = input()
list1 =[]
for i in NN:
  if i == '0':
    list1.append('0')
  elif i == '1' :
    list1.append('1')
  else:
    if len(list1) == 0:
      pass
    else:
      list1.pop(-1)
for i in list1:
  print(i,end ='')