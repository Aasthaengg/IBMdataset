from collections import deque
S = input()

def calculate(s):
    q = deque()
    for i in range(len(s)):

        if s[i] == "0":
            q.append("0")
            continue

        if s[i] == "1":
            q.append("1")
            continue

        if s[i] == "B":
            if len(q) > 0:
                q.pop()


    if len(q) == 0:
        print("(empty)")
    else:
        print("".join(list(q)))


calculate(S)
