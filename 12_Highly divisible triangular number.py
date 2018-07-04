Triangle=[]
Start=1
sum=0
count=1

while count<500:
    count=1
    sum=sum+Start
    Triangle.append(sum)
    i=2
    sum1=sum
    while i <= sum1:
        k=0;
        while sum1%i == 0:
            sum1 = sum1 / i
            k = k + 1
        if k!=0:
            count=count*(k+1)
        i = i + 1
    Start+=1
print(max(Triangle))
