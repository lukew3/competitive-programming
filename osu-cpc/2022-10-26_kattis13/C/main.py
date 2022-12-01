r, c, n = map(int, input().split())
coords = [[0] * c] * r
print(coords)
for _ in range(n):
    x, y = map(int, input())
    coords[y][x] = 1
    

