w = input()
while len(w) > 0:
    a = w[0]
    if w.count(a)%2 != 0:
        print("No")
        exit()
    w = w.replace(a,"")
print("Yes")