a,b=map(int,input().split())
num=0

if a%2==0 and b%2==1 or a%2==1 and b%2==0:
  num=1
  
if a>0 and b>0 or a<0 and b<0 and num==1:
  print("Positive")
  
elif a<0 and b<0 and num==0 or a<0 and b<0:
  print("Negative")
  
else:
  print("Zero")