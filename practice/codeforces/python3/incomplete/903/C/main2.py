boxesCount = int(input())
boxes = input().split()
boxesList = []
for box in boxes:
    boxesList.append(int(box))
boxes = boxesList
visible = len(boxes)

filledBoxes=[]
emptyBoxes=boxes
allBoxes = emptyBoxes + filledBoxes

complete = False
while complete == False:
    isEmpty=False
    tempList = allBoxes
    smallest = 1000000000
    for item in filledBoxes:
        if item < smallest:
            smallest = item
    for item in emptyBoxes:
        if item < smallest:
            smallest = item
            isEmpty=True

    #tempList.remove(smallest)
    if isEmpty==False:
        tempList = emptyBoxes
    elif isEmpty == True:
        tempList == emptyBoxes.remove(smallest)
        emptyBoxes.append(smallest)

    tempSmallest = 1000000000
    for item in tempList:
        if item < tempSmallest and item > smallest:
            tempSmallest = item

    if tempSmallest > smallest and tempSmallest != 1000000000:
        #print(boxes)
        #boxes = boxes.remove(smallest)
        if isEmpty == True:
            emptyBoxes.remove(smallest)
            filledBoxes.append(tempSmallest)
        elif isEmpty == False:
            filledBoxes.remove(smallest)
        visible -= 1
    else:
        complete = True


print(visible)
