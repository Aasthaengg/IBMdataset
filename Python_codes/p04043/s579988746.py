a = input().split()
sums = 0
for i in a:
    sums += int(i)

if sums == 17:
    print("YES")
else:
    print("NO")