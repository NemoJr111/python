f = open("myfile.txt", "a+")
print('enter text ')

while str!="@":
    str = input()
    if str!='@':
        f.write(str+"\n")
        f.seek(0,0)
        print('the contents are')
        str=f.read()
        print(str)
f.close()