def sim(p_aisles, a_isles):

    pass    

def main():
    n, k = map(int, input().split())
    p_aisles = [False] * n
    a_aisles = [False] * 2
    for _ in range(k):
        idd, dirr = input().split()
        if idd == 'A':
            a_aisles[0] = dirr
        elif idd == 'B':
            a_aisles[1] = dirr
        else:
            p_aisles[int(idd)-1] = dirr


    return 1

print(main())

"""
If A and B are the same direction, 1 or zero possible combinations exist

If both A and B are not facing the same direction, all permutations of rows are possible
    plus when A and B are facing the same direction

Impossible if side aisle and last aisle pointing towards non-enter/exit
"""
