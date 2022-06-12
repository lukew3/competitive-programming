test = [1, 2, 3, 4, 5]
test2 = [3, 2, 1]

def solution(my_input):
    out_list = []
    for i in range(len(my_input)):
        result = 1
        for j in range(len(my_input)):
            if j != i:
                result = result * my_input[j]
        out_list.append(result)
    return out_list

print(solution(test))
print(solution(test2))
