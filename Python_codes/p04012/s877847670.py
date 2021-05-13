s = input()
alp=[0 for i in range(0, 28)]
for j in s:
	if j>='a' and j<='z':
		alp[(ord(j)-ord('a'))]=alp[(ord(j)-ord('a'))]+1
f=0
for i in range(0 ,26):
	if alp[i]%2!=0:
		f=1
if f==1:
	print("No")
else:
	print("Yes")