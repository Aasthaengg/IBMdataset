l = list(map(int, input().split()))

flag_5 = flag_7 = 0

for i in l:
    if i == 5:
        flag_5 += 1
    if i == 7:
        flag_7 += 1

if flag_5 == 2 and flag_7 == 1:
    print("YES")
else:
    print("NO")
