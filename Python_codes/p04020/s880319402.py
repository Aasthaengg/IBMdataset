import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = []
for i in range(n):
    lst1.append(int(readline()))

ans = 0
lst2 = []
for i in lst1:
    i -= 2
    if i >= 0:
        ans += (i+1)//2
    if i == -2:
        lst2.append(0)
    elif even(i):
        lst2.append(2)
    else:
        lst2.append(1)

now = 0
while now < n:
    if now == 0:
        if lst2[now] == 2:
            ans += 1
            lst2[now] = 0
        now += 1
        continue
    if lst2[now-1] == 1 and lst2[now] == 2:
        ans += 1
        lst2[now] = 1
        now += 1
        continue

    if lst2[now-1] == 1 and lst2[now] == 1:
        ans += 1
        lst2[now] = 0
        now += 1
        continue
    
    if lst2[now] == 2:
        ans += 1
        lst2[now] = 0
        now += 1
        continue
    now += 1

print(ans)