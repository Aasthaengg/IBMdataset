s = list(input())

i = 0
while i < len(s):
    if s[i] == "B":
        if i == 0:
            del s[0]
            i -= 1
        else:
            del s[i-1:i+1]
            i -= 2

    i += 1

print("".join(s))