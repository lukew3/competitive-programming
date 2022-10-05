def gap_perms(size, opposite):
    pass    

def sn_sn(a):
    for i in range(1, len(a)+1):
        if i % 2 == 0 and (a[i] != '' or a[i] != 'W2E'):
            return 0
        elif i % 2 != 0 and (a[i] != '' or a[i] != 'E2W'):
            return 0
    return 1

def ns_ns(a):
    # when a and b are n2s
    for i in range(1, len(a)+1)[::-1]:
        # check from last row to first
        pass



def main():
    n, k = map(int, input().split())
    p_aisles = [''] * n
    a_aisles = [''] * 2
    for _ in range(k):
        idd, dirr = input().split()
        if idd == 'A':
            a_aisles[0] = dirr
        elif idd == 'B':
            a_aisles[1] = dirr
        else:
            p_aisles[int(idd)-1] = dirr
    
    if (p_aisles[0] == 'W2E' and B == 'N2S') or (p_aisles[-1] == 'E2W' and B == 'S2N'):
        return 0
    elif a_aisles[0] == 'N2S' and a_aisles[1] == 'N2S':
        # ensure all product aisles in order when a and b are n2s
        for i in range(1, n+1)[::-1]:

    elif a_aisles[0] != '' and a_aisles[0] == a_aisles[1]:
        for i in range(n):
            

    elif A != '' and B != '':
        if A == B:
            # If A and B are the same direction, 1 or zero possible combinations exist
            pass
        else:
            # All perms are possible, customers just have to walk more when going up than going down
              # Unless there is no lower row pointing towards upwards access aisle
    print(p_aisles)

    return 1

print(main())

"""
If A and B are the same direction, 1 or zero possible combinations exist

If both A and B are not facing the same direction, all permutations of rows are possible
    plus when A and B are facing the same direction

Impossible if side aisle and last aisle pointing towards non-enter/exit

Can never stem from or point towards a non-entrace/exit corner
"""
