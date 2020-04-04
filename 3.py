sum=0
list=[12,23,24]
for x in list:
    sum=0
    i=x
    while x>0:
        num=x%10
        sum=sum+num
        x=x//10
    print("sum of digits of",i,"=",sum)