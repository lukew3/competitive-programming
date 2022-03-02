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
    pageCount1 = 0
    countedChapters = []
    while (chapter in refDict):
        pageCount1 += pagesArr[chapter-1]
        countedChapters.append(chapter)
        chapter = refDict[chapter]
    pageCount1 += pagesArr[chapter-1]
    countedChapters.append(chapter)
    for chapter2 in cchapters:
        if chapter != chapter2:
            pageCount2 = 0
            while (chapter2 in refDict and chapter2 not in countedChapters):
                pageCount2 += pagesArr[chapter2-1]
                chapter2 = refDict[chapter2]
            pageCount2 += pagesArr[chapter2-1]
            if pageCount1 + pageCount2 < minPageCount:
                minPageCount = pageCount1 + pageCount2

print(minPageCount)
