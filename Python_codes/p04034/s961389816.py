n, m = map(int, input().split())
ball = [1] * n  # 各箱のボールの個数。初めは各箱に１つずつ。
red = set([0])  # 赤いボールがある可能性のある箱のインデックス。初めは0番目の箱に赤いボールがある。
for _ in range(m):
  x, y = map(int, input().split())
  ball[x-1] -= 1  # x-1番目の箱のボールを1つ減らす
  ball[y-1] += 1  # y-1番目の箱のボールを1つ増やす
  if x-1 in red:  # x-1番目の箱に赤いボールがあるなら、y-1番目の箱に移動したとする。
  	red.add(y-1)
  if ball[x-1] == 0:  # x-1番目の箱にボールがなくなったら、赤いボールもないはずなので
    red.discard(x-1)  # 可能性のある箱から削除しとく
print(len(red))  # 可能性のある箱の個数を出力