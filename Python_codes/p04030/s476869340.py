s = list(str(input()))
answer = ""

for i in s:
    if i == "0":
        answer = answer + "0"

    elif i == "1":
        answer = answer + "1"

    elif i == "B":
        answer = answer[:-1]

print(answer)
