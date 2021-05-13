w = input()
for i in w:
    if w.count(i) %2 != 0:
        print("No")
        exit()
print("Yes")