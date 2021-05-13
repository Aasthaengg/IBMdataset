#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

w = input()

for s in w:
    if (w.count(s) % 2 != 0):
        print("No")
        exit()

print("Yes")
