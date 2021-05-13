def main():
    from collections import deque
    s = list(input())
    ans = deque([])
    for i in s:
        if i == '0':
            ans.append('0')
        elif i == '1':
            ans.append('1')
        else:
            if len(ans)!= 0:
                ans.pop()

    print(''.join(ans))

main()