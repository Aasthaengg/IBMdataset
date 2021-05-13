N = int(input())
listA = [int(input()) for i in range(N)]
count = 0

for x in range(N):
    check = listA[x]
    count += check // 2
    if x != N - 1 and check % 2 != 0:
        if listA[x + 1] > 0:
            count += 1
            listA[x + 1] -= 1
print(count)
