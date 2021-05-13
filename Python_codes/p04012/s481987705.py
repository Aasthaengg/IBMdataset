w = input()
wl = list(w)
wu = list(set(wl))
wu_len  = len(wu)
counter = 0
for wo in wu:
  if wl.count(wo) % 2 == 0:
    counter+=1
  else:
    break
if counter == int(wu_len):
  print("Yes")
else:
  print("No")