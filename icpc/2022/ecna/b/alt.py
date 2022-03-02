n, m = map(int, input().split())
minPageCount = int(1e8) #maxint
pagesArr = []
while len(pagesArr) < n:
    pagesArr += [int(num) for num in input().split()]

refDict = {}
cchapters = [i + 1 for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    refDict[b] = a
    if a in cchapters: # remove prereqs from cchapters if present
        cchapters.remove(a) 

for chapter in cchapters:
    pageCountA = 0
    countedChapters = []
    while (chapter in refDict):
        pageCountA += pagesArr[chapter-1]
        countedChapters.append(chapter)
        chapter = refDict[chapter]
    for chapter2 in cchapters:
        if chapter != chapter2:
            pageCountB = pageCountA
            while (chapter2 in refDict and chapter2 not in countedChapters):
                pageCountB += pagesArr[chapter2-1]
                chapter2 = refDict[chapter2]
            if pageCountB < minPageCount:
                minPageCount = pageCountB

print(minPageCount)
