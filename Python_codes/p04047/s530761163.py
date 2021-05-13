wood = input()

lis_1 = list(map(int,input().split()))

lis_1.sort()

guzai = 0

for i in range(int(wood)):
  max_gu = min(lis_1[2*i],lis_1[2*i+1])
  guzai += int(max_gu)
print(guzai)


