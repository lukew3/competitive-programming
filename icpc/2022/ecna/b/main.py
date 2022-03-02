n, m = map(int, input().split())
minPages = 1000 ** 2
pagesArr = []
while len(pagesArr) < n:
    pagesArr += input().split()

refDict = {}
cchapters = [i + 1 for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    refDict[b] = a
    if a in cchapters: # remove prereqs from cchapters if present
        cchapters.remove(a) 

def getPages(chapter, prev):
    if chapter in prev:
        return 0, []
    elif chapter in refDict:
        pagecount, prev2 = getPages(refDict[chapter], prev)
        return int(pagesArr[chapter-1]) + pagecount, [chapter] + prev2
    else:
        return int(pagesArr[chapter-1]), [chapter]

for chapter in cchapters:
    pages, prevRead = getPages(chapter, [])
    for chapter2 in cchapters:
        if chapter != chapter2:
            pages2, _ = getPages(chapter2, prevRead)
            if pages + pages2 < minPages:
                minPages = pages + pages2

print(minPages)
