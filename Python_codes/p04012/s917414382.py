s = input()
l = []
for i in range(len(s)):
	l.append(s.count(s[i]))
r = []
for x in l:
	if(x%2!=0):
		r.append(False)
	else:
		r.append(True)

if(all(r)):
	print("Yes")
else:
	print("No")
