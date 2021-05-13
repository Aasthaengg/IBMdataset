def main():
    s = input()
    from collections import deque
    c = deque()
    for i in s:
        if i == 'B':
            if c:
                c.pop()
        else:
            c.append(i)
    print(''.join(list(c)))

if __name__ == '__main__':
    main()
