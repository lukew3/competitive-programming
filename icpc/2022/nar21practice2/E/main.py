def main():
    d, t, c, r = map(int, input().split())
    clouds = []
    roofs = []
    for _ in range(c):
        clouds.append(list(map(int, input().split())))
    for _ in range(r):
        roofs.append(list(map(int, input().split())))
    for s in range(t):

