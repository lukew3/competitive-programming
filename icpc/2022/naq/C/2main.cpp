import math
from fractions import Fraction as frac

def f(n):
    # get factors of n
    factors = []
    for i in range(2, math.floor(n)+1): # don't need to check for factors after n/2
        if n % i == 0:
            factors.append(i)
    c = 0
    # check each number in [1, n) to see if it shares a factor
    for i in range(1, n):
        for factor in factors:
            if i%factor == 0:
                c += 1
                break
    c += 1 # add this for n = itself
    return c


def g(n):
    p = f(n)
    return p, n

def main():
    n = int(input())
    mp = 0
    mq = 1
    for i in range(2, n):
        p, q = g(i)
        if (p/q) > (mp/mq):
            mp = p
            mq = q
    print(mp, mq)
    print(frac(mp, mq))


main()
