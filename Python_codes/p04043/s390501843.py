# 整数の入力
a, b, c = map(int, input().split())
# 合計17でないときNOを出力
if not (a+b+c == 17):
    print("NO")
    exit()
# 7を含まないときNOを出力
if not 7 in (a, b, c):
    print("NO")
    exit()
# 5を含まないときNOを出力、それ以外はYESを出力
if not 5 in (a, b, c):
    print("NO")
    exit()
else:
    print("YES")