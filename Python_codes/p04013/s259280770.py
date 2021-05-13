import sys
n, a  = [int(i) for i in sys.stdin.readline().split()]
x_ls = [int(i) - a for i in sys.stdin.readline().split()]
#memo_ls[i][j] : i番目まででj - 50*50ができる通り数
memo_ls = [[0 for i in range(2 * 50 * 50 + 1)] for j in range(n+1)]
memo_ls[0][50*50] = 1
for i, x in enumerate(x_ls, 1):
    for j in range(2*50*50+1):
        memo_ls[i][j] =  memo_ls[i-1][j]
        if 0 <= j - x <= 2*50*50:
            memo_ls[i][j] += memo_ls[i - 1][j - x]
print(memo_ls[-1][50*50] - 1)