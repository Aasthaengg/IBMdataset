import collections #Counterを使いたいから

c = collections.Counter(list(input())) #出現回数が多い順に要素を取得 キーと値

f = True
for val in c.values():
  if val%2==1:
    f = False
if f:
  print("Yes")
else:
  print("No")