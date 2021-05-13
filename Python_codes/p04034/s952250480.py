boxnum, sousanum = map(int, input().split(" "))
sousa = []
for i in range(sousanum):
  sousa.append(list(map(int, input().split(" "))))

#aka[0][0] ...[ボール個数][赤フラグ]
ball = [[1, 0] for i in range(boxnum)]
ball[0][1] = 1
for i in range(sousanum):
  if ball[sousa[i][0] - 1][1] == 1:#赤色あり
    ball[sousa[i][1] - 1][1] = 1
    
  ball[sousa[i][0] - 1][0] -= 1
  ball[sousa[i][1] - 1][0] += 1
  
  if ball[sousa[i][0] - 1][0] == 0:#ボール尽きた
    ball[sousa[i][0] - 1][1] = 0
total = 0
for i in range(boxnum):
    total += ball[i][1]
print(total)