def add(*args):
    sum = 0
    for num in args:
        sum+=num
    return sum

result= add(1,2,3)
print('sum is ', result)
result = add(10,20,30,40,50)
print('sum is ', result)
result = add(6,8,10,12)
print('sum is ', result)