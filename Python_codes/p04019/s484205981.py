s = input()

check = [0]*4

for i in range(len(s)):
    if s[i] == "N" and check[0] == 0:
        check[0] = 1
    if s[i] == "S" and check[1] == 0:
        check[1] = 1
    if s[i] == "W" and check[2] == 0:
        check[2] = 1
    if s[i] == "E" and check[3] == 0:
        check[3] = 1
if check[0] == check[1] and check[2] == check[3]:
    print("Yes")
else:
    print("No")