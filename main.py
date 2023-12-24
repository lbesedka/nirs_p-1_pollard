import math
import numpy as np

a = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def pollards_p_1(N, B):
    d = 1
    index = 0
    while d == 1:
        for j in range(2, B):
            a_ind = a[index]
            a_j = int((np.power(a_ind, j)) % N)
            d = math.gcd((a_j - 1), N)
            if (d != 1) and (1 < d < N):
                return d
        index += 1
        if(a[index] == 23):
            return d
            break


def get_B(B):
    return int(np.power(B, 2))


def factorization(N, B):
    d = pollards_p_1(N, B)
    if d == 1:
        B = get_B(B)
        d = pollards_p_1(N, B)
        if d == 1:
            print("prime")
            exit()
    p = d
    q = int(N / p)
    return p, q


if __name__ == '__main__':
    N = 168441398857
    B = 1000
    p, q = factorization(N, B)
    print("p = ", p, "q = ", q)

