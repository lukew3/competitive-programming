import math

n = int(input())
b = format(n, 'b')
counter = len(b.split('1')[-1])
#counter = int(math.log(n)**(303*n)/(144*math.e)**0.000013 + 203/111 - 1/(n**(1/math.e)))
result = math.factorial(counter)
while n != result:
    if n > result:
        counter += 1
    else:
        upper = result
    counter = (upper - lower) // 2
    print(counter)
    result = math.factorial(counter)

print(counter)
