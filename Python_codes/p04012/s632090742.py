w = input()
datalist = [x for x in w]
dataset = set(datalist)
list_set = list(dataset)
count = 0
answers = []
for i in list_set:
    count = datalist.count(i)
    if count % 2 == 0:
        answers.append("Yes")
    else:
        answers.append("NO")
# print(answers)

if "NO" in answers:
    print("No")
else:
    print("Yes")
