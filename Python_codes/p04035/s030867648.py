import sys
from collections import deque
import copy
import math
def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [N, L] = [int(input_raw[0]), int(input_raw[1])]
    input_raw = read_func().strip().split()
    A = [int(input_raw[i]) for i in range(N)]
    B = deque([A[i] + A[i + 1] for i in range(N - 1)])
    sumA = sum(A)
    s_idx = 1
    t_idx = len(B)
    seq = []
    for i in range(N - 1):
        if sumA < L:
            print "Impossible"
            return
        if B[len(B) - 1] < L:
            B.pop()
            sumA -= A[t_idx]
            seq.append(t_idx)
            t_idx -= 1

        else :
            B.popleft()
            sumA -= A[s_idx - 1]
            seq.append(s_idx)
            s_idx += 1
        if len(seq) == N - 1:
            break

    print "Possible"
    for i in range(len(seq)):
        print seq[i]





if __name__ == '__main__':
    main()
