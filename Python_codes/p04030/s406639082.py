def resolve():
    s = input()
    display_str = ""
    for i in range(len(s)):
        if s[i] == "B":
            if len(display_str) != 0:
                display_str = display_str[0:-1]
        else:
            display_str += s[i]
    print(display_str)

resolve()