S = input()
output = ''
for s in S:
    if s == '0' or s == '1':
        output += s
    else:
        l = len(output)
        if l > 0:
            output = output[:l-1]
print(output)
