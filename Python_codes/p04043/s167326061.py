mylist = list(map(int,input().split()))
x = mylist.count(5)
y = mylist.count(7)
 
if x == 2 and y == 1:
  print("YES")
else:
  print("NO")