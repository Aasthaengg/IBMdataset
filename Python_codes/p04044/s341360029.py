N, L = map(int, input().split())
input_line1 = [input() for i in range(N)]
input_line2 = []
for i in range(N):
	input_line2.append(min(input_line1))
	input_line1.remove(min(input_line1))
print("".join(input_line2))