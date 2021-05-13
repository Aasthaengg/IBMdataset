S=str(input())
T=''
for i in range(len(S)):
    if S[i]=='0' or S[i]=='1':
        T+=S[i]
    else:
        T=T[:-1]
print(T)