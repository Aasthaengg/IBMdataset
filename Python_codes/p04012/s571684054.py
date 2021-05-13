w=input()
S=set(w)
print("Yes" if all(w.count(s)%2==0 for s in S)==True else "No")
