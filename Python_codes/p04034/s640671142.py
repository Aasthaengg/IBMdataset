N, M, *xy = map(int, open(0).read().split())
boxes = [{"count": 1, "red": False} for _ in range(N)]
boxes[0]["red"] = True

for x, y in zip(*[iter(xy)] * 2):
    x -= 1
    y -= 1
    if boxes[x]["red"]:
        boxes[y]["red"] = True
        if boxes[x]["count"] == 1:
            boxes[x]["red"] = False
    boxes[x]["count"] -= 1
    boxes[y]["count"] += 1
print(sum(b["red"] for b in boxes))
