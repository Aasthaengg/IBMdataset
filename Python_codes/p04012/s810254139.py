w = list(input())
ww = list(set(w))

for i in range(len(ww)):
    num = w.count(ww[i])
    if num % 2 != 0:
        print("No")
        break
else:
    print("Yes")