s = list(input())
word = []
for i in range(len(s)):
    if s[i] == "B":
        if len(word) != 0:
            del word[len(word)-1]
    else:
        word.append(s[i])
Ans = ""
for i in range(len(word)):
    Ans += word[i]
print(Ans)