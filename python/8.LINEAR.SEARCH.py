from array import *
x=array('I',[])
print('enter the limit:')
n=int(input())
print('\nenter the elements:')
for i in range(n):
    x.append(int(input()))
print('enter the element to search:')
s=int(input())
for i in range(n):
    if x[i]==s:
        print('\nFound at position ',i+1)
        break
else: 
    print('Not found!')