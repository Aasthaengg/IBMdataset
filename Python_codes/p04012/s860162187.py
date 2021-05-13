w = input()

cher_count = {}

for c in w:
    if c in cher_count:
        cher_count[c] += 1
    else:
        cher_count[c] = 1

for num in cher_count.values():
    if num % 2 != 0:
        print("No")
        break
else:
    print("Yes")