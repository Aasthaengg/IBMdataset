w = input()
tf = True

for i in range(len(w)):
    if w.count(w[i]) % 2 != 0:
        tf = False
        break

if tf:
    print("Yes")
else:
    print("No")