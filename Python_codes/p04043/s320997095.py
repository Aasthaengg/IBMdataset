l = list(map(int, input().split()))
seven = 0
five = 0
for i in l:
    if i == 5:
        five += 1
    if i == 7:
        seven += 1

if five == 2 and seven == 1:
    print("YES")
else:
    print("NO")