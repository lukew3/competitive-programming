n, m = map(int, input().split())
# max pages is max chapters * max pages per chapter
minPages = 1000 ** 2
# pagesArr stores the page counts for each chapter
pagesArr = []
# must use a while loop to handle input because input can be on multiple lines
while len(pagesArr) < n:
    pagesArr += input().split()

# refDict holds key value pairs where the value is the chapter required by the key
refDict = {}
# cchapters is initially a list of all chapters numbered 1 to n
cchapters = [i + 1 for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    # add each reference pair to refDict
    refDict[b] = a
    # if requested chapter is in cchapters, remove it so that only those chapters that are not requested by anything are in cchapters
    if a in cchapters:
        cchapters.remove(a) 

# recursive function getPages gets the number of pages for each chapter and the chapters that it requires as well as a list of chapters that have been counted
def getPages(chapter, prev):
    # if chapter previously counted, count 0 pages and don't return any chapters
    if chapter in prev:
        return 0, []
    # if chapter has a dependency, run getPages to get the pages in the dependency and chapters counted. Return this plus the number of pages in the current chapter and the current chapter
    elif chapter in refDict:
        pagecount, prev2 = getPages(refDict[chapter], prev)
        return int(pagesArr[chapter-1]) + pagecount, [chapter] + prev2
    # if chapter doesn't have a dependency, return the number of pages in the chapter and the chapter number
    else:
        return int(pagesArr[chapter-1]), [chapter]

for chapter in cchapters:
    # get pages and chapters read while reading that chapter
    pages, prevRead = getPages(chapter, [])
    for chapter2 in cchapters:
        # for each chapter in cchapters that are not equal to the previously parsed chapter
        if chapter != chapter2:
            # get number of pages rea dwhen satisfying that chapter and don't record the chapters satisfied, since that is not needed
            pages2, _ = getPages(chapter2, prevRead)
            # check if total pages read is minimum and set minPags if it is
            if pages + pages2 < minPages:
                minPages = pages + pages2

print(minPages)
