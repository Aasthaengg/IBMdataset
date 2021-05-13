#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]


s = input()

ans = []

for i in range(len(s)):
    if s[i] != "B":
        ans.append(s[i])
    else:
        if (len(ans) > 0):
            ans = ans[:-1]

for i in range(len(ans)):
    print(ans[i], end="")


