N = int(input())
lList = [int(x) for x in input().split()]

lList.sort()

result = 0
for l, ll in zip(lList[::2], lList[1::2]):
    result += min(l,ll)

print(result)