num5 = 0
num7 = 0

a, b, c = (int(x) for x in input().split())

if (a == 5):
    num5 = num5 +1
elif (a == 7):
    num7 = num7 +1

if (b == 5):
    num5 = num5 +1
elif (b == 7):
    num7 = num7 +1

if (c == 5):
    num5 = num5 +1
elif (c == 7):
    num7 = num7 +1

if (num5 == 2) and (num7 == 1):
    print("YES")
else:
    print("NO")
