S_Num,End_Num=1,20
End_Num1=End_Num
primeNum=[]
Final=[]
while End_Num>=S_Num:
	Found=0
	if End_Num%2!==0:
		i=int(End_Num/2)
		while i>1:
			if End_Num%i==0:
				Found=1;break;
			i=i-1
		if Found==0 and End_Num!=1:
			primeNum.append(End_Num)
	End_Num=End_Num-1

for Num in primeNum:
	prod=1
	while prod<=End_Num1:
		prod=prod*Num
	Final.append(prod/Num)
	
from functools import reduce
print(reduce(lambda x,y:x*y,Final))
