n = int(input())
As = list(map(int, input().split()))

total = 0
for i in range(n):
    total += As[i]

# detect optimal number
ave = total / n

if ave != int(ave):
    if ave >= int(ave)+0.5:
        ave = int(ave)+1
    else:
        ave = int(ave)

ans = 0
for i in range(n):
    ans += (ave-As[i])**2

print(int(ans))