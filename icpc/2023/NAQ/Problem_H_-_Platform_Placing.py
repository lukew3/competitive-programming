n, s, l = map(int, input().split())
f = []
for _ in range(n):
    f.append(int(input()))
f.sort()

d = []
if n == 1:
    print(l)
    exit(0)
    
for i in range(n - 1):
    d.append(f[i + 1] - f[i])

if s > min(d):
    print(-1)
    exit(0)

boards = [s] * n
for i in range(n):
    boards[i] = [f[i] - s/2, f[i] + s/2]


zeroethBoardL = min(l/2, boards[1][0] - f[0])
boards[0] = [f[0] - zeroethBoardL, f[0] + zeroethBoardL]


for i in range(1, n - 1):
    maxL = min(l/2, f[i] - boards[i - 1][1], boards[i + 1][0] - f[i])
    boards[i] = [f[i] - maxL, f[i] + maxL]

lastBoardL = min(l/2, f[-1] - boards[-2][1])
boards[-1] = [f[-1] - lastBoardL, f[-1] + lastBoardL]
print(int(sum([boards[i][1] - boards[i][0] for i in range(n)])))
# print(boards)



