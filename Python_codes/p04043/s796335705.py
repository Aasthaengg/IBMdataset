# coding:utf-8


def main():
    haiku = [5, 7, 5]
    word_num = input().split(' ')
    for num in word_num:
        try:
            haiku.remove(int(num))
        except:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    reply = main()
    print(reply)
