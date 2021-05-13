Count = [0,0,0,0]
for j in input():
    if j == 'N':
        Count[0] +=1
    elif j == 'S':
        Count[1] +=1
    elif j == 'W':
        Count[2] +=1
    elif j == 'E':
        Count[3] +=1

if (Count[0] > 0 and Count[1] > 0) and (Count[2] > 0 and Count[3] > 0):
    print("Yes")
elif (Count[0] == 0 and Count[1] == 0) and (Count[2] > 0 and Count[3] > 0):
    print("Yes")
elif (Count[0] > 0 and Count[1] > 0) and (Count[2] == 0 and Count[3] == 0):
    print("Yes")
else:
    print("No")
