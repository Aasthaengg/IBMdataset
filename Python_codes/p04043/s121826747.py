a,b,c=map(int,input().split())
if a+b+c==17 and max(a,b,c)==7 and min(a,b,c)==5:
  print("YES")
else:
  print("NO")