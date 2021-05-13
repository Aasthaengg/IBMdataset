a,b = map(int,input().split())
#０が含まれていたら0.あとは負の数で場合分け
if a<=0 and 0<=b:
  print("Zero")
  
elif a>0 and b>0:
  print("Positive")

elif a<0 and b<0:
  number = abs(a-b)+1
  if number%2 == 0:
    print("Positive")
  else:
    print("Negative")