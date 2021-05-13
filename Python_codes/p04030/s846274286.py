def main():
    a=[]
    for s in input():
        if s == "B":
            if len(a) > 0:
                a.pop()
        else:
            a.append(s)
    print("".join(a))
    pass

if __name__ == "__main__":
    main()