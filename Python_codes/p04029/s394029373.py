# A - キャンディーとN人の子供イージー

# 一人目にはキャンディーを一個、二人目には二個、N人目にはN個あげていくと
# 必要なキャンディーは合計何個か？

child = int(input())

answer = int(child * (child + 1) / 2)

print(answer)
