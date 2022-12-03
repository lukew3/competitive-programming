import sys

score = 0
for line in sys.stdin:
    a, b = line.split()
    if b == 'X':
        score += 1
        if a == 'A':
            score += 3
        elif a == 'C':
            score += 6
    elif b == 'Y':
        score += 2
        if a == 'B':
            score += 3
        elif a == 'A':
            score += 6
    elif b == 'Z':
        score += 3
        if a == 'C':
            score += 3
        elif a == 'B':
            score += 6
print(score)

