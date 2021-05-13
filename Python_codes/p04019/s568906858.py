st = input()
if "N" in st:
    if ("S" in st) is False:
        print("No")
        exit()
if "W" in st:
    if ("E" in st) is False:
        print("No")
        exit()
if "S" in st:
    if ("N" in st) is False:
        print("No")
        exit()
if "E" in st:
    if ("W" in st) is False:
        print("No")
        exit()
print("Yes")