import sys
def input(): return sys.stdin.readline().strip()

def main():
    s = input()
    ans = ""
    for c in s:
        if c != 'B':
            ans += c
        elif ans != "":
            ans = ans[:-1]
    print(ans)

if __name__ == "__main__":
    main()
