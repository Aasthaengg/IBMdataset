s = list(set(input()))
l = [["N","S"], ["W","E"], ["N", "S", "W", "E"]]
if len(s) != 2 and len(s) != 4:
    print("No")
    exit()
for i in l:
    x = 0
    for j in s:
        if j in i:
            x += 1
    if x == len(i):
        print("Yes")
        exit()
print("No")