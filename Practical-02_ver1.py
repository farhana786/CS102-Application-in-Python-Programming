'''
Name : Mohammed Ismail
Roll no. : 673
Batch : F3
Problem 1 : Write a Python program for following conditions.
If n is single digit print square of it.
If n is two digit print square root of it.
If n is three digit print cube root of it.
'''


num = int(input('Enter the number : '))
if num>0 and num <10 : # testcondition 1
	print(num," is one digit number")#these statements executes when test condidion1 is true othewise control will jump to next elif block
	print("The square of ",num,"is : ",num**2)

elif num>9 and num<100 : #testcondition 2
	print(num," is a two digit number")#these statements executes when test condidion2 is true othewise control will jump to next elif block
	print("Square root of ",num, "is : ",round(num**0.5, 2))
	
elif num>99 and num<1000 : #testcondition3
	print(num," is a three digit number")#these statements executes when test condidion3 is true othewise control will jump to next elif block
	print("Cube root of ",num,"is : ",round(num**(1/3) ,2))

else :
	print("Entered no. is a zero or negative number")

	
'''
OUTPUT
Enter the number : 20
20  is a two digit number
Square root of  20 is :  4.47

[Program finished]
'''

'''
Problem 2 : Calculate electricity bill by taking number of units consumed by end user in Kilowatt hour (units)
 For normal consumers,
Units consumed under 200units, rate =2.5rs/unit
 For distributors,
Units consumed between 201-450 units,
Rate = 3.5rs,
 For industrial area,
Units consumed 450+,
Rate =4.5rs
'''


unit = int(input("Enter the consumed units : "))
if unit <= 200 :
	print("The electricity is used for house hold purpose")
	print("The electricity bill is : ", unit*2.5, " Rs.")
	
elif unit>200 and unit<=450 :
	print("The electricity is used for distribution purposeby  distributor")
	print("The electricity bill is : ", unit*3.5," Rs.")
	
elif unit>450 :
	print("The electricity is used in industrial area")
	print("The electricity bill is : ", unit*4.5, " Rs.")

		
'''
OUTPUT
Enter the consumed units : 300
The electricity is used for distribution purposeby  distributor
The electricity bill is :  1050.0  Rs.

[Program finished]
'''

'''
Problem 3 : Write a program in python to calculate the profit and loss percentage of a electronic device seller. take the input as selling price as SP and cost price as CP . If SP>CP then he will have profit and the calculate the profit percentage as {(SP - CP)/CP}*100 and if CP>SP then he will have loss and then calculate the loss % as {(CP-SP}/SP}*100 . then display his loss or profit.
'''

CP=int(input("Enter the cost price of electric device : ₹ "))

SP=int(input("Enter the selling price of electric device : ₹ "))

if SP>CP :
	print("The seller get profit of  ₹ ",SP-CP)
	print("The percentage profit he gets is ",((SP-CP)/CP)*100,"%")
	
else :
	print("The seller suffers from loss of  ₹ ", CP-SP)
	print("The percentage of loss is ",((CP-SP)/SP)*100,"%")
		
'''
OUTPUT
Enter the cost price of electric device : ₹ 250
Enter the selling price of electric device : ₹ 200
The seller suffers from loss of  ₹  50
The percentage of loss is  25.0 %

[Program finished]
'''

'''
Problem 4 : Write a program in python to calculate the interest bank should charge for various EMI options. If the user chooses to EMI plan for 3 month then bank should charge interest @5% per month .if he choose EMI plan for 6 months then Rate will be 10% per month and if he chooses EMI plan for 12 month then the rate will be 15% per month . use the formula I=(P*R*T)/100 to calculate the interest and then claculate the total amount he will be charged at the end of his Plan . take input P principal amount that is the amount he wants to pay in EMI .R as the rate which bank chares and T as the month plan . take T in year not in month . T = month/12.
'''
p=int(input("How much amout you want to invest : ₹ "))
t=int(input("Time period for which you want to invest in months : "))

if t==3 :
	
	print("Investor recieves an intrest of ₹ ", (((p*5)*t)/100))
	print("The amount recieved by the investor is ₹ ", (((p*5)*t)/100) + p)
	
elif t==6 :
	print("Investor recieves an intrest of ₹ ", (((p*10)*t)/100))
	print("The amount recieved by the investor is ₹ ", (((p*10)*t)/100) + p)
	
else :
	print("Investor recieves an intrest of ₹ ", (((p*15)*t)/100))
	print("The amount recieved by the investor is ₹ ", (((p*15)*t)/100) + p)

'''
OUTPUT
How much amout you want to invest : ₹ 2000
Time period for which you want to invest in months : 6
Investor recieves an intrest of ₹  1200.0
The amount recieved by the investor is ₹  3200.0

[Program finished]
'''