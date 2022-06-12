#https://codeforces.com/contest/122/problem/A
num = input()
luckynums = [4, 7, 47, 74]
islucky = True
for char in num:
    if char != "4" and char != "7":
        islucky=False
        break
    else:
        islucky=True
for luckynum in luckynums:
    if int(num) % luckynum == 0:
        islucky=True
        break
if islucky:
    print("YES")
else:
    print("NO")
