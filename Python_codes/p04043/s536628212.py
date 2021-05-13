a,b,c=map(int,input().split())

N5=0
N7=0

if a==5:
  N5 +=1
elif a==7:
    N7 +=1

if b==5:
  N5 +=1
elif b==7:
    N7 +=1
    
if c==5:
  N5 +=1
elif c==7:
    N7 +=1
    
if (N5==2)*(N7==1):
  print('YES')
else:
    print('NO')
