ga1, gb1, ga2, gb2 = map(int, input().split())
ea1, eb1, ea2, eb2 = map(int, input().split())
# Sum the averages of each die
g = (ga1+ga2)/2 + (gb1+gb2)/2
e = (ea1+ea2)/2 + (eb1+eb2)/2
if (g > e):
    print('Gunnar')
elif (e > g):
    print('Emma')
else:
    print('Tie')
