S=input()
for s in S:
  if S.count(s) %2 == 1:
    print("No")
    break
else:
  print("Yes")