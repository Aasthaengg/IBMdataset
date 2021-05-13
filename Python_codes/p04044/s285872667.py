s = input().split()
number = int(s[0])
length = int(s[1])

words = []

for num in range(number):
    x = input()
    words.append(x)

words.sort()

for num in words:
    print(num, end='')
