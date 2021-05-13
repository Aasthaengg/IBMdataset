s = input()

while s.count("B") != 0:
    if s[0] == "B":
        s = s[1:]
    else:
        i = s.index("B")
        s = s[:i-1] + s[i+1:]
print(s)