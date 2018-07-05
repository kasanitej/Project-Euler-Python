#I complicated few things, but didnt rectify it due to lost interest

Dict1={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
Dict2={10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
length=0
for Num in range(1,1001): #len(str(Num)) gives us the number of digits
    if(Num<10):
        length=length+len(Dict1[Num])
    if(Num>9 and Num<100):
        if Num in Dict2.keys():
            length=length+len(Dict2[Num])
        else:
            length=length+len(Dict2[int(str(Num)[0]+str(0))]+Dict1[int(str(Num)[1])]) #Not adding spaces
    if(Num>99 and Num<1000):
        if(int(str(Num)[1])==0 and int(str(Num)[2])==0): #X00
            length=length+len(Dict1[int(str(Num)[0])]+'hundred')
        elif(int(str(Num)[1])==0 and int(str(Num)[2])!=0): #X0Y
            length=length+len(Dict1[int(str(Num)[0])]+'hundredand'+Dict1[int(str(Num)[2])])
        elif(int(str(Num)[1])!=0 and int(str(Num)[2])==0): #XY0
            length=length+len(Dict1[int(str(Num)[0])]+'hundredand'+Dict2[int(str(Num)[1:3])])
        elif(int(str(Num)[1])==1):#X1Y
            length=length+len(Dict1[int(str(Num)[0])]+'hundredand'+Dict2[int(str(Num)[1:3])])
        else:
            length=length+len(Dict1[int(str(Num)[0])]+'hundredand'+Dict2[int(str(Num)[1]+str(0))]+Dict1[int(str(Num)[2])])
    if(Num==1000):
        length=length+11

print(length)
