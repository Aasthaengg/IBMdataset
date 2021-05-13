s=input()
x,y=0,0
li=s
if 'N' in li and 'S' in li and not 'E' in li and not 'W' in li:
  print('Yes')
  exit()
  
if 'E' in li and 'W' in li and not 'S' in li and not 'N' in li:
  print('Yes')
  exit()
 
for i in s:
    if(i=='N'):
        y+=1
    elif(i=='S'):
        y-=1
    elif(i=='W'):
        x-=1
    else:
        x+=1
if(x==0 and y==0):
    print("Yes")
else:
    print("No")
