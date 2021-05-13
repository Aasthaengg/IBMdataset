s = input().split()

a = s[0]
b = s[1]
c = s[2]

five_count = 0
seven_count = 0

if a == '5':
    five_count += 1
elif a == '7':
    seven_count += 1

if b == '5':
    five_count += 1
elif b == '7':
    seven_count += 1

if c == '5':
    five_count += 1
elif c == '7':
    seven_count += 1

if five_count == 2 and seven_count == 1:
    answer = 'YES'
else:
    answer = 'NO'

print(answer)
