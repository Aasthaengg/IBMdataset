X = input()
text = []

for i in X:
    if i == 'B':
        text = text[:-1]
    else:
        text.append(i)
print(*text, sep='')