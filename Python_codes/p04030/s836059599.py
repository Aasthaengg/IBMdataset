
s = input()
c = list(s)
ans_list = []

for i in range(len(s)):
    if(c[i]=="0" or c[i]=="1"):
        ans_list.append(c[i])
    else:
        try:
            ans_list.pop(-1)
        except:
            a = 0

print("".join(ans_list))
