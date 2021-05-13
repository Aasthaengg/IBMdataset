string = input()
news = "NEWS"
flg = [False for _ in range(4)]
for s in string:
    for i in range(4):
        if s == news[i]:
            flg[i] = True
            break
if flg[0] != flg[3] or flg[1] != flg[2]:
    print("No")
else:
    print("Yes")