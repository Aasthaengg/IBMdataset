n_5 = 0
n_7 = 0

a = map(int, input().split())
for i in a:
    if i == 5:
        n_5 += 1
    elif i == 7:
        n_7 += 1

if n_5 == 2 and n_7 == 1:
    print("YES")
else:
    print("NO")