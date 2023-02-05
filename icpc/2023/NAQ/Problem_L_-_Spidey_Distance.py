from fractions import Fraction

t, s = map(int, input().split())

def taxi(n):
    return 4 * int(n*(n+1)/2) + 1

def spidey(n):
    return int(taxi(n) + 2 * (n//3) * (2*(n%3 + 1) + 3*(n//3 - 1)))

"""
for i in range(1, 11):
    print(taxi(i))
"""

taxi_points = taxi(t)
overlap_points = taxi(t)
spidey_points = spidey(s)

if 3 * t >= 4 * s:
    print(1)
elif t > s:
    overlap_points = taxi(s)
    for i in range(t-s):
        overlap_points += 4 * (s - 3 * i - 2)
    print(Fraction(overlap_points, spidey_points))
else:
    overlap_points = taxi(t)
    print(Fraction(overlap_points, spidey_points))
