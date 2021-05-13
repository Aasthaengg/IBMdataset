import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,*A = map(int,read().split())

rest = 0
answer = 0
for x in A:
    if not x:
        rest = 0
        continue
    if rest:
        x -= 1
        answer += 1
    q,rest = divmod(x,2)
    answer += q

print(answer)