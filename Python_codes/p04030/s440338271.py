S=input()

T=""
for s in S:
    if s=="B":
        if T:
            T=T[:-1]
    else:
        T+=s
print(T)
