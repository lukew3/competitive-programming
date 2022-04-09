fun_scores = []
point_to_i = {}

def min_path(nodeId):
    smallest = 10**9
    bestRemoveNodes = []
    for parent in point_to_i[nodeId]:
        val, removeNodes = min_path(parent)
        if val < smallest:
            smallest = val
            bestRemoveNodes = removeNodes
    if smallest == 10**9:
        smallest = 0
    bestRemoveNodes.append(nodeId)
    smallest = max(fun_scores[nodeId], smallest)
    return smallest, bestRemoveNodes

def removeNextLeaf():
    #find a leaf
    for node in point_to_i:
        isLeaf = True
        for node2 in point_to_i:
            if node in point_to_i[node2]:
                #node is not leaf
                isLeaf = False
                break
        if isLeaf:
            s, removeNodes = min_path(node)
            score = 0
            for removeNode in removeNodes:
                score = max(score, fun_scores[removeNode])
                if removeNode in point_to_i:
                    point_to_i.pop(removeNode)
            for nextNodeId in point_to_i:
                for parent in point_to_i[nextNodeId]:
                    if parent in removeNodes:
                        point_to_i[nextNodeId].remove(parent)
        return score

t = int(input())
for case in range(t):
    n = int(input())
    # The id of a module is its index in f and p plus 1
    fun_scores = [0] + [int(j) for j in input().split()]
    p = [int(j) for j in input().split()]
    point_to_i = {}
    for i in range(n):
        point_to_i[i+1] = []
    for j in range(n):
        if p[j] != 0:
            point_to_i[p[j]] += [j+1]
    score = 0
    while (len(point_to_i) != 0):
        score += removeNextLeaf()
    print(f"Case #{case+1}: " + str(score))



