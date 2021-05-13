S=input()
S=sorted(set(S))
if S.count("N")==1:
	if S.count("S")==0:
		print("No")
		exit()
if S.count("S")==1:
	if S.count("N")==0:
		print("No")
		exit()
if S.count("E")==1:
	if S.count("W")==0:
		print("No")
		exit()
if S.count("W")==1:
	if S.count("E")==0:
		print("No")
		exit()
print("Yes")