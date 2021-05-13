n = int(input())
a = sorted(list(map(int,input().split())))
sum = 0
List_sum = []
Counter = []
Count_num = (a[-1] - a[0])+1
for i in range(Count_num):
    Counter.append(a[0]+i)
    if Counter[-1] == a[-1]:
        break
if len(set(a)) == 1:
    print(0)
else:
    for i in Counter:
        for j in a:
            sum += (i-j)**2
        else:
            List_sum.append(sum)
            sum = 0
    else:
        print(min(List_sum))