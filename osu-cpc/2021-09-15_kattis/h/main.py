import math
m, n = map(int, input().split())
s = 0
r = 0
cs = []
for i in range(n):
    c = int(input())
    cs.append(c)
    s += c
d = s-m #difference between what we want and what we have
u = d%n #unfortunates who get less than everybody else
b = math.trunc(d/n) #number of candies not received by the more fortunate children
cs.sort()
index = 0
while cs[index] < b:
    r += cs[index]**2
    d -= cs[index]
    n -= 1
    b = math.trunc(d/n) 
    index+=1
u = d%n 
r += u*((b+1)**2)+(n-u)*(b**2)
print(r)
