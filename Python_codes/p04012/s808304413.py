w = input()
count = [0] * 27

for i in range(len(w)):
	count[ord(w[i])-97] += 1

for i in range(len(count)):
	if count[i] % 2 != 0:
		print("No")
		exit()

print("Yes")