# coding: utf-8

a, b= map(int,input().split())
table = []
ans = ""
for i in range(a):
    table.append(input())
list.sort(table)
for i in range(a):
    ans += table[i]
print(ans)