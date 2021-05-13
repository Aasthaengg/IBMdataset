def resolve():
    S = input()
    chk = set(S)
    if len(chk) != 4:
        if ("N" in chk and "S" not in chk) or ("E" in chk and "W" not in chk) or (
                "S" in chk and "N" not in chk) or ("W" in chk and "E" not in chk):
            print("No")
            return
    print("Yes")


resolve()
