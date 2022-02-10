def findword(w, g):
    for char in w:
        for row in g:
            for gridchar in row:
                if char == gridchar:

def findLetter(x, y, 

def main():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    n = int(input())
    for _ in range(n):
        word = input()
        findword(word, grid)

