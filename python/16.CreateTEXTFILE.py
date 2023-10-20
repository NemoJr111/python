f = open("myfile.txt", "w")
print('enter text (@ to save and quit)')

while str!='@':
    str = input()
    if str!='@':
        f.write(str+"\n")
f.close()