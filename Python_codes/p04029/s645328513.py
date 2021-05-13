input_num = int(input())

# 取得した Nから必要なキャンディーの個数を算出し出力する
i = 1
result = 0;

while i <= input_num:
    result = result + i
    i = i + 1

print(result)