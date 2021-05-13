def resolve():
    w = input()
    w_list = list(w)
    for char in set(w_list):
        if w.count(char) % 2 == 1:
            print("No")
            return
    print("Yes")

resolve()