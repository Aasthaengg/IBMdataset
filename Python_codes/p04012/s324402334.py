w=input()

while True:
  w1=w[0]
  s=w.count(w1)
  if s%2!=0:
    print("No")
    break
  w=w.replace(w1,"")
  if w=="":
    print("Yes")
    break