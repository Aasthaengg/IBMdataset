s = input()
r = ""
for i in s:
	if i == '0':
		r = r+'0'
	elif i == '1':
		r = r+'1'
	else:
		r = r[0:len(r)-1]

print(r)