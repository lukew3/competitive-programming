from sys import stdin

case = 0
for line in stdin:
    has4 = False
    line = line.rstrip()
    if line.find('4') != -1:
        case = case+1
        has4 = True
    num1 = []
    num2 = []
    for char in line:
        if char == '4':
            char = str(int(char)-1)
            other = str(1)
        else:
            other = str(0)
        num1.append(char)
        num2.append(other)
        fin1 = ''.join(num1)
        fin2 = ''.join(num2)
        fin2 = str(int(fin2))
    if has4==True:
        print("Case #" + str(case) + ": " + fin1 + " " + fin2)
