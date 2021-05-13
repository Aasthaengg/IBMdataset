S = input()
T = ""
for s in S:
  if s == "0":
    T += "0"
  elif s == "1":
    T += "1"
  elif len(T)>0:
    T = T[:-1]
print(T)