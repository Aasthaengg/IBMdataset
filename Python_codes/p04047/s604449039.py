N = int(input())
print(sum(l for l in sorted(list(map(int,input().split())),reverse=True)[1::2]))