import sys

d = []
first = input()
for char in first:
    if char == '0':
        d.append(-1)
    else:
        d.append(1)
for line in sys.stdin:
    for i in range(len(line)-1):
        if line[i] == '0':
            d[i] -= 1
        else:
            d[i] += 1
gamma = ""
epsilon = ""
for item in d:
    if item < 0:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(int(gamma, 2) * int(epsilon, 2))

