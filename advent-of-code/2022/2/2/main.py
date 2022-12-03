import sys

score = 0
for line in sys.stdin:
    a, b = line.split()
    if b == 'X':
        if a == 'A':
            score += 3
        elif a == 'B':
            score += 1
        elif a == 'C':
            score += 2
    elif b == 'Y':
        score += 3
        if a == 'A':
            score += 1
        elif a == 'B':
            score += 2
        elif a == 'C':
            score += 3
    elif b == 'Z':
        score += 6
        if a == 'A':
            score += 2
        elif a == 'B':
            score += 3
        elif a == 'C':
            score += 1
print(score)

