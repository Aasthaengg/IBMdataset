s = input()

output = ''
for i in s:
    if i == '0':
        output += '0'
    elif i == '1':
        output += '1'
    elif i == 'B' and len(output) != 0:
        output = output[:len(output) - 1]
print(output)
