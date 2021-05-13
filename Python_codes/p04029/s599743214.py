# A - キャンディーとN人の子供イージー
# N+(N-1)+....

# 子供の人数を入力
child_number = int(input())
# print(child_number)

# 計算
answer = int(child_number * (child_number + 1) / 2)

# 表示
print(answer)