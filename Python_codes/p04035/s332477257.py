NL = input()
NL = "".join(NL).rstrip("\n").split(" ")
N = int(NL[0])
L = int(NL[1])
a = input()
a = "".join(a).split(" ")

for s in range(N-1):
	if int(a[s])+int(a[s+1])>=L:
		Last = s+1
		print("Possible")
		for s in range(N-1):
			if s+1>Last:
				for j in range(N):
					if (N-1-j) ==s:
						#print(Last)
						break
					print(N-1-j)
				break
			if s+1==Last:
				continue
			print(s+1)
		print(Last)
		break
	if s==N-2:
		print("Impossible")