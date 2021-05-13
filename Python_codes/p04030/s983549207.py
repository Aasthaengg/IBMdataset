S = input()

res = ""
for i in range(len(S)):
    if(S[i] == "B" and res != ''):
        res = res[:-1]
    elif(S[i] == "0"):
        res += "0"
    elif(S[i] == "1"):
        res += "1"
print(res)
