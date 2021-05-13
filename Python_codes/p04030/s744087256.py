s = input()
str = ''
for char in s:
    if char == '0' or char == '1':
        str += char
    elif char == 'B':
        if str:
            str = str[:-1]
        else:
            continue

print(str)