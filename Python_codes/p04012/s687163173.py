w = input()

for i in set(w):
    if not w.count(i)%2 == 0:
        print("No")
        exit(0)

print("Yes")