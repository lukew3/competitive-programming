n = int(input())
l=[]
for _ in range(n):
    l.append(int(input()))

def solution(plates, cur_weight):
    best = 0
    for i in range(len(plates)-1):
        print(plates)
        print(i)
        next_weight = cur_weight+plates[i]
        next_plates = plates
        next_plates.pop(i)
        if abs(1000-next_weight) < abs(1000-best):
            best = next_weight
        if len(next_plates) == 0:
            continue
        else:
            solution(next_plates, next_weight)
    return best

print(solution(l, 0))
