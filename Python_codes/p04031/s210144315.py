n = int(input())
a = list(map(int, input().split()))

a.sort()

def cost(a, y):
    ans = 0
    for i in a:
        ans += (i - y) * (i - y)
    return ans

# binary search

left = a[0]
right = a[n-1]

while left < right:
    center = (left + right) // 2
    if cost(a, center) < cost(a, center+1):
        right = center
    else:
        left = center + 1

print(cost(a, left))