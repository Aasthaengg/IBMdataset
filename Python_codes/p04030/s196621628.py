S=input()
List = list(S)
res=""

def responseB(moji):
  if moji == "":
    return moji
  else:
    moji = moji[0:len(moji)-1]
    return moji

for i in range(len(S)):
  if not List[i] == "B":
    res += List[i]
  else:
    res = responseB(res)
print(res)