line = input()
answ = ''
for s in line:
    if s != 'B':
        answ += s
    else:
        answ = answ[:len(answ)-1]
print(answ)
