n,l = map(int,input().split())

word_list = []

for i in range(n):
    word_list.append(input())

answer = ''.join(sorted(word_list))
print(answer)