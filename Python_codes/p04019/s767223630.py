import collections

def main():
    S = list(input())
    Sset = set(S)
    if len(Sset) in [1, 3]:
        print('No')
    elif Sset == set(['S', 'N']) or Sset == set(['W', 'E']):
        print('Yes')
    elif len(Sset) == 4:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
