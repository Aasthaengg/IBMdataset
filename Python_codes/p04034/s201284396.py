n, m = map(int, input().split())
nums = [1 for _ in range(n)]
tf = [False for _ in range(n)]
tf[0] = True

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    nums[x] -= 1
    nums[y] += 1
    if tf[x]:
        tf[y] = True
        if nums[x] == 0:
            tf[x] = False
print(tf.count(True))