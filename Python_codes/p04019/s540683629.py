s = input()
answer = "Yes"
if "N" in s and "S" not in s:
	answer = "No"
elif "S" in s and "N" not in s:
	answer = "No"
elif "W" in s and "E" not in s:
	answer = "No"
elif "E" in s and "W" not in s:
	answer = "No"
print(answer)
