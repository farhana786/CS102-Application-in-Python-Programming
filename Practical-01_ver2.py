#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Name:Nausheen Aftab
Batch:F3
Roll:656
'''

'''
Problem Statement1:
To accept an object mass in kilograms and velocity in meters per second and 
display its momentum and energy. Momentum=mc, Energy=mc2 where m is the mass 
of the object and c is its velocity.
'''

# #is used for single line comments
# ''' ''' are used to enclose muti-line comments
 
print("\tW E L C O M E\tT O\tO U R\tP R O G R A M") #To print something print("statement") keyword is used and statements to be printed are inclosed in "" or '' comas.

obj=input("\n\n Enter the object name : ") #we can directly store the value in a variable and to take input from the user input keyword is used and statements to be printed with are enclosed in "" or '' comas in () parnthesis.
print("\n\n To calculate the Momentum and Energy of",obj)#it doesn't require format specifier,to print something stored in variable we just need to mention the variable name after , 

m=float(input("\n\n Enter its Mass in Kilograms : "))#by default the input is taken as a string to convert it into an float vlaue we need to use float typecaste before input keyword 
print(" Mass of the ",obj," is :",m,"kg")

c=float(input("\n Enter its velocity of the in meters per second : "))
print(" Velocity of the ",obj," is :",c,"m/s")

momentum=m*c # * symbol is used for multiplication  
energy=m*c**2 # c**2 means c raise to the power 2

print("\n Momentum of the ",obj," is :",momentum,"kgm/s")
print("\n Energy of the ",obj," is :",energy,"Joules")

print("\n\n\t\tEnd\tof\tthe\tProgram")

print("\n\n\t\t\tT H A N K\tY O U") # Ending statements

'''
O U T P U T
________________________________________________________________________

W E L C O M E	T O	O U R	P R O G R A M


 Enter the object name : Ball


 To calculate the Momentum and Energy of Ball


 Enter its Mass in Kilograms : 0.5
 Mass of the  Ball  is : 0.5 kg

 Enter its velocity of the in meters per second : 9.86
 Velocity of the  Ball  is : 9.86 m/s

 Momentum of the  Ball  is : 4.93 kgm/s

 Energy of the  Ball  is : 48.60979999999999 Joules


		End	of	the	Program


			T H A N K	Y O U
________________________________________________________________________

'''

'''
____________________________________________________________________________________
'''

'''
Problem Statement2:
Calculate heat generated in a conductor of resistance 200 ohm if current is 
flowing for User input time and value of current flowing for user input amps
'''

print("\tW E L C O M E\tT O\tO U R\tP R O G R A M") # Welcoming statements

print("\n\n To calculate Heat Generated in a Conductor ") #topic

R=200 #values assigned to variable r, here whatever type of value assigned to the variable is taken as its data type
I=int(input("\n\n Enter the value current : ")) #here int typcaste is used
t=int(input("\n Enter the time duration : "))

print("\n\n The resistance of the conductor is ",R,"ohms")
print(" The current flowing through the conduntor is ",I,"amperes")
print(" We want to calculate the Heat generated for ",t,"seconds")

heat=(I**2)*R*t #heat is calculated

print("\n\n Heat Generated in the conductor of ",R,"ohms resistance is ",heat,"Joules")

print("\n\n\t\tEnd\tof\tthe\tProgram")

print("\n\n\t\t\tT H A N K\tY O U") #Ending Statement

'''
O U T P U T
______________________________________________________________________________

	W E L C O M E	T O	O U R	P R O G R A M


 To calculate Heat Generated in a Conductor 


 Enter the value current : 10

 Enter the time duration : 90


 The resistance of the conductor is  200 ohms
 The current flowing through the conduntor is  10 amperes
 We want to calculate the Heat generated for  90 seconds


 Heat Generated in the conductor of  200 ohms resistance is  1800000 Joules


		End	of	the	Program


			T H A N K	Y O U
______________________________________________________________________________
'''

'''
________________________________________________________________________________________________
'''

'''
Problem Statement3
A Crash Test is being conducted. Enter the Car detail using input function. 
Also Calculate the initial speed, acceleration of the car if the final velocity
is zero in time 10s and distance of track is 20 m
'''

print("\tW E L C O M E\tT O\tO U R\tP R O G R A M") #Welcoming Statement

print("\n\n Crash Test Results ") #Topic

date=input("\n Enter date of Crash Test in DDMMYYYY format : ") #date
model=input(" Enter the type of the Car : ") #Car details
name=input(" Enter name of the Car ") #Car details

s=20 # assigning values to the variable
t=10 # assigning values to the variable
v=0 # assigning values to the variable

a=40/(t**2) # a is calculated
u=a*4 # u is calculated

print("\n Acceleration of the Car is ",a,"m/s^2") #output
print(" Initial Speed of the Car is ",u,"m/s") #output

print("\n\n\t\tEnd\tof\tthe\tProgram")

print("\n\n\t\t\tT H A N K\tY O U") #ending statements

'''
O U T P U T
_________________________________________________________________________________

	W E L C O M E	T O	O U R	P R O G R A M


 Crash Test Results 

 Enter date of Crash Test in DDMMYYYY format : 01062021
 Enter the type of the Car : Sports
 Enter name of the Car Lamborghini

 Acceleration of the Car is  0.4 m/s^2
 Initial Speed of the Car is  1.6 m/s


		End	of	the	Program


			T H A N K	Y O U
_________________________________________________________________________________
'''
'''
_____________________________________________________________________________________________________
'''

'''
Problem Statement4:
Find the area of plots to build housing society . take input from user is 
length and breadth of the site in Meter. and area is in meter square.
'''

print("\tW E L C O M E\tT O\tO U R\tP R O G R A M") #Welcoming Statement
 
print("\n\n To find the Area of plot to buid housing society ") #Topic

length=int(input("\n Enter the length of the plot in meters : ")) #taking input from the user
breadth=int(input(" Enter the breadth of the plot in meters : ")) #taking input from the user

print("\n The Length of the plot is",length,"m") #statements
print(" The Breadth of the plot is",breadth,"m") #statements

area=length*breadth # calculating area 

print("\n The Area of the plot is",area,"m^2") #output

print("\n\n\t\tEnd\tof\tthe\tProgram")

print("\n\n\t\t\tT H A N K\tY O U") #ending statement

'''
_______________________________________________________________________________

	W E L C O M E	T O	O U R	P R O G R A M


 To find the Area of plot to buid housing society 

 Enter the length of the plot in meters : 94
 Enter the breadth of the plot in meters : 113

 The Length of the plot is 94 m
 The Breadth of the plot is 113 m

 The Area of the plot is 10622 m^2


		End	of	the	Program


			T H A N K	Y O U
_______________________________________________________________________________
'''

