data = input().split()

seven = 0
five = 0

for i in range(len(data)):
	if int(data[i]) == 7:
		seven += 1
	elif int(data[i]) == 5:
		five +=1

if seven == 1 and five == 2:
	print('YES')
else:
	print('NO')