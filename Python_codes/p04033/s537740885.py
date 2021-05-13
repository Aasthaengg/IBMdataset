def resolve():
    '''
    code here
    '''
    a,b = [int(item) for item in input().split()]

    if a > 0:
        print('Positive')
    else:
        if a <= 0 and 0 <= b:
            print('Zero')
        else:
            cnt = b - a + 1

            if cnt % 2 == 0:
                print('Positive')
            else:
                print('Negative')

if __name__ == "__main__":
    resolve()
