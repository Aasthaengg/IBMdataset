n=int(input())
print(sum(sorted([int(i) for i in input().split()])[-2::-2]))