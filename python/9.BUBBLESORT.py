from array import *
x=array('I',[])
print('enter the limit:')
n=int(input())
print('enter the elements:')
for i in range(n):
    x.append(int(input()))
for i in range(n-1):
    for j in range(n-i-1):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
print('Sorted array is ',x)
