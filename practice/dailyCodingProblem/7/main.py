def solution(message):
    val = 1
    for i in range(len(message)-1):
        if int(message[i]+message[i+1]) <= 26:
            val += solution(message[i+2:])
    return val

# Test
print(solution('111')) # 3
print(solution('1211')) # 5
