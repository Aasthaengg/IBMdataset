s = input()

n = len(s)
s_ans = ""

for i in range(n):
    if s[i] == "0":
        s_ans = s_ans + "0"

    elif s[i] == "1":
        s_ans = s_ans + "1"

    elif s[i] == "B":
        len_ans = len(s_ans)
        if len_ans >= 1:
            s_ans = s_ans[:len_ans-1]

        elif len_ans == 0:
            s_ans = s_ans

        else:
            print("error2")

    else:
        print("error1")

print(s_ans)