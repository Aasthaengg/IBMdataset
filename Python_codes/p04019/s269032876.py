s = input()
flag = True
if ("N" in s) ^ ("S" in s):
    flag = False
if ("W" in s) ^ ("E" in s):
    flag = False
if flag == True:
    print("Yes")
else:
    print("No")