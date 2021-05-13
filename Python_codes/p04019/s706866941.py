S = input()

if "N" in S:
    if "S" not in S:
        print("No")
    elif "E" in S:
        if "W" not in S:
            print("No")
        else:
            print("Yes")
    else:
        if "W" in S:
            print("No")
        else:
            print("Yes")


else:
    if "S" in S:
        print("No")
    elif "E" in S:
        if "W" not in S:
            print("No")
        else:
            print("Yes")
    else:
        if "W" in S:
            print("No")
        else:
            print("Yes")