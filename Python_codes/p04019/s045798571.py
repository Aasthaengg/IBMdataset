s = input()

ans1 = (("S" in s) and ("N" in s)) or (("S" not in s) and ("N" not in s))
ans2 = (("E" in s) and ("W" in s)) or (("E" not in s) and ("W" not in s))

print("Yes" if ans1 and ans2 else "No")