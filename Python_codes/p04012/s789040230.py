w = input()

group = set(w)

count = []
for i in group:
    count.append(w.count(i))

ans = 0

for j in count:
    if j % 2 == 1:
        ans = 1
    else:
        pass

if ans == 0:
    print("Yes")
else:
    print("No")