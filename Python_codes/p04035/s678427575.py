import sys
readline = sys.stdin.readline

N,L = map(int,readline().split())
A = list(map(int,readline().split()))

# 2個でL以上の隣合うペアがどこかにあれば、そこを最後に残せば大丈夫
target = -1
for i in range(1,len(A)):
  if A[i] + A[i - 1] >= L:
    target = i
    break
if target == -1:
  print("Impossible")
  exit(0)

left = []
for i in range(1,target):
  left.append(i)
  
right = []
for i in range(len(A) - 1,target,-1):
  right.append(i)

print("Possible")
for l in left:
  print(l)
for r in right:
  print(r)
print(target)