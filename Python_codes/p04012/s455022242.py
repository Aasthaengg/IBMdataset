w = str(input())
count = 0
for i in w:
    if w.count(i) % 2 == 0:
        pass
    else:
        count = 1
        break
print("Yes" if count == 0 else "No")