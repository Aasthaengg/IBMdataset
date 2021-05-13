from collections import Counter


def answer(w: str) -> str:
    counts = Counter(w).values()
    for count in counts:
        if count % 2 == 1:
            return 'No'

    return 'Yes'

def main():
    w = input()
    print(answer(w))

if __name__ == '__main__':
    main()
