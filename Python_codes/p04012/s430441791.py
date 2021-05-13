w = sorted(input())
elements = set(w)

check = 0

for e in elements:
  if w.count(e)%2 != 0:
    check = 1


if check == 0:
    print("Yes")
else:
    print("No")