input_line = list(input())
t = []
for i in input_line:
	if i == "0":
		t.append("0")
	elif i == "1":
		t.append("1")
	else:
		if t == []:
			t == []
		else:
			t.pop(-1)
print("".join(t))