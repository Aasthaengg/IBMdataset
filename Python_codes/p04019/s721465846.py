def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

s = s()

cn,cs,ce,cw = 0,0,0,0
for i in range(len(s)):
	if s[i] == "N":
		cn = 1
	elif s[i] == "S":
		cs = 1
	elif s[i] == "E":
		ce = 1
	else:
		cw = 1

if (cn and cs) and (ce and cw):
	print("Yes")
elif (cn and cs) and not(ce or cw):
	print("Yes")
elif not(cn or cs) and (ce and cw):
	print("Yes")
else:
	print("No")