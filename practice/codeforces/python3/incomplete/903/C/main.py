#INCOMPLETE

boxesCount = int(input())
boxes = input().split()
boxesList = []
for box in boxes:
    boxesList.append(int(box))
boxes = boxesList
visible = len(boxes)

filledBoxes=[]
emptyBoxes=boxes

complete = False
while complete == False:
    tempList = boxes
    smallest = 1000000000
    for item in boxes:
        if item < smallest:
            smallest = item
    tempList.remove(smallest)
    tempSmallest = 1000000000
    for item in tempList:
        if item < tempSmallest and item > smallest:
            tempSmallest = item
    if tempSmallest > smallest and tempSmallest != 1000000000:
        boxes = tempList
        visible -= 1
    else:
        complete = True
print(visible)
