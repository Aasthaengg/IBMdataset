W = input()
f = True
for w in set(W):
    if W.count(w) % 2 != 0:
        f = False
if f:
    print("Yes")
else:
    print("No")