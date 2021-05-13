S = input()

Z = []
X = len(S)

i = 0
while i  < X :
    if S[i] == "0":
        Z.append(0)
    elif S[i] == "1":
        Z.append(1)
    elif S[i] == "B":
        if len(Z)== 0:
            pass
        else:
            Z.pop()
    i += 1

i = 0
X = len(Z)
while i < X:
    print(Z[i] , end ="")
    i +=1