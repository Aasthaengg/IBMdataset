s=input()
s=set(s)
s=sorted(s)
ans=[['E','W'],['N','S'],['E','N','S','W']]
print("Yes" if s in ans else "No")