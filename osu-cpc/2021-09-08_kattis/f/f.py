a=input()
b=a.split()
c=0
for w in b:
    if 'ae' in w:
        c+=1
if c/len(b) >= .4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
