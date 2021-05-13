s = input()
ss =set(s)
cnt = 0
for i in ss:
  if s.count(i)%2 !=0:
    cnt =1
print("Yes" if cnt ==0 else "No")