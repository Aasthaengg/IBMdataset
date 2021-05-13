s = input()
s = s[::-1]
news = ""
c = 0
for i in range(len(s)):
    if s[i] == "B":
        c += 1
    elif c == 0:
        news += s[i]
    else:
        c -= 1
print(news[::-1])