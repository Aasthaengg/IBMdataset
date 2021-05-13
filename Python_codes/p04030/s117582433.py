s = input()

i = list(s)

answer = []

for num in i:
    if num == '0':
        answer.append(num)
    elif num == '1':
        answer.append(num)
    else:
        if answer == []:
            continue
        else:
            answer.pop()

for num in answer:
    print(num,end='')