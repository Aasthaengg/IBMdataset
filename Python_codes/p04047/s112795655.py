#  --*-coding:utf-8-*--

N = int(input())
L = sorted(map(int, input().split()))

print(sum(min(L[2*i], L[2*i+1]) for i in range(N)))
