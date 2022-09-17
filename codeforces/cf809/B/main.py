t = int(input())
for _ in range(t):
    n = int(input())
    c = [int(i) for i in input().split()]
    for r in range(1, n+1):
        # To increase stack, need even number of elements between each occurence of r
        # Extend right until first element found
        h = 0 # height
        mh = 0 # max height
        if r in c:
            i = c.index(r)
            h = 1
            mh = 1
            while i != -1:
                if r in c[i+1:]:
                    ni = c.index(r, i+1) # next index of i
                    if (ni - i + 1) % 2 == 0:
                        h += 1
                        if h > mh:
                            mh = h
                    else:
                        if r in c[ni+1:]:
                            nni = c.index(r, ni + 1) # next next index of i
                            if (nni - i + 1) % 2 == 0:
                                h += 1
                                ni = nni
                                if h > mh:
                                    mh = h
                            else:
                                h = 1
                        else:
                            h = 1
                    i = ni
                else:
                    break
        print(mh, end=' ')
    print()
