m=int(input('enter the numeric value: '))
print('Prime numbers under',m,'are:')
for n in range(2,m):
    for i in range(2,n):
        if n%i==0: 
            break
    else:
        print(n)