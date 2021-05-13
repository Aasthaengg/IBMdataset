n = [int(i) for i in input().split()]
seven = 0
five = 0
if n[0] == 5:
    five += 1
if n[0] == 7:
    seven += 1
if n[1] == 5:
    five += 1
if n[1] == 7:
    seven += 1
if n[2] == 5:
    five += 1
if n[2] == 7:
    seven += 1
if five == 2 and seven == 1:
    print("YES")
else:
    print("NO")