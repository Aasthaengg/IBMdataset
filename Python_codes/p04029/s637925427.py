# 入力
n = int(input())
# result初期化
result = 0
# １からNまで繰り返し
for i in range(1,n+1):
    # 等差数列
    count = i
    result = result + count
# 結果を表示
print(result)