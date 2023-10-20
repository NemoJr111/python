num=eval(input('enter elements in []\n'))
sum=0
n=len(num)
for i in range(n):
 sum+=num[i]
 
print('\nSum = ',sum)
print('Average = ',sum/n)