#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
NAME : MOHAMMED ISMAIL
ROLL NUMBER: 673
BATCH :F3

'''




'''PROBLEM STATEMENT 1:
    
    To accept an object mass in kilograms and velocity in meters per second and display its momentum and energy. Momentum=mc,
    Energy=mc2 where m is the mass of the object and c is its velocity.
'''
print(" Good morning sir, I will help you find the momentum and energy of an object , just enter the mass and velocity in standard units i.e kg and m/s for mass and velocity respectively ")
mass=int(input("Enter the mass of object in kilogram:"))
vel=int(input("Enter the velocity of object in meter per second:"))
mom=mass*vel  
en=mom*vel
#assigning values to kg,vel and mom variables...

print("Momoentum of the entered object whose mass is :",mass,"kg and velocity is :",vel,"m\s is \n:",mom,"m\s")
print("Energy of the object is",en,"Joule")


'''
OUTPUT FOR PROBLEM STATEMENT 1:

Good morning sir, I will help you find the momentum and energy of an object , just enter the mass and velocity in standard units i.e kg and m/s for mass and velocity respectively 
Enter the mass of object in kilogram:5
Enter the velocity of object in meter per second:4
Momoentum of the entered object whose mass is : 5 kg and velocity is : 4 m\s is 
: 20 m\s
Energy of the object is 80 Joule
'\nOUTPUT FOR PROBLEM STATEMENT 1:\nEnter the mass of object in kilogram:5\nEnter the velocity of object in meter per second:4\nMomoentum of the entered object whose mass is : 5 kg 
and velocity is : 4 m\\s is \n: 20 m\\s\nEnergy of the object is 80 Joule\n'
'''

'''

 PROBLEM STATEMENT 2 :
  Calculate heat generated in a conductor of resistance 200 ohm 
  if current is flowing for User input time and value of current flowing for user input amps.

'''
print("Good Morning Mr. Stark!!! Welcome after your exploration in C ,\n I will help you to calculate heat generated in a conductor by using H=i^2RT but by using Python !!!")

R=200 
i=float(input("Enter the current flowing through the conductor in ampere:"))
t=float(input("Enter the time for which current is flowing through conductor in seconds :"))


H=i**2*R*t
h=H/4.18

print("The heat generated in the conductor is:\n",H,"Joule or", h,"calorie" )
'''
OUTPUT OF PROBLEM STATEMENT 2:

Good Morning Mr. Stark!!! Welcome after your exploration in C ,
 I will help you to calculate heat generated in a conductor by using H=i^2RT but by using Python !!!
Enter the current flowing through the conductor in ampere:4.18
Enter the time for which current is flowing through conductor in seconds :4
The heat generated in the conductor is:
 13977.919999999998 Joule or 3344.0 calorie
 
'''
'''
PROBLEM STATEMENT 3: A Crash Test is being conducted.
Enter the Car detail using input function. Also Calculate the initial speed, acceleration of the car 
if the final velocity is zero and distance of track is 20 m.
'''

# HERE WE WILL UTILISE THE CONCEPT OF RETARDATION AND APPLY EQUATIONS OF KINEMATICS ...
# WE KMOW THAT,WHEN THE ACCELERATION IS CONSTANT;v+u=2S/t ...WHERE v=FINAL VELOCITY; u=INITIAL VELOCITY 
# HERE ACCELERATION WILL BE NEGATIVE AS IT IS RETARDED MOTION
print("Good Morning Mr MI\nWelcome to your virtual crash test studio\n JARVIS at your service Sir !!!\n Enter the time in which the car stop to calculate the initial velocity and retadation\n KINDLY MAKE SURE YOU ENTER TIME IN SECONDS TO AVOID SYSTEM OF UNITS ERROR")
t=float(input("Enter the time in which car stopped :"))
s=20
v=0
# Given values...
print("Final velocity=0 m/s\ntime taken to stop car is",t,"s\ndistance covred=20m")
u=2*s/t
a=u/10      
print("Initial velocity=",u,"m/s")
print("Acceleration is :",-a,"m/s^2")

'''
OUTPUT OF PROBLEM STATEMENT 3:
Good Morning Mr MI
Welcome to your virtual crash test studio
 JARVIS at your service Sir !!!
 Enter the time in which the car stop to calculate the initial velocity and retadation
 KINDLY MAKE SURE YOU ENTER TIME IN SECONDS TO AVOID SYSTEM OF UNITS ERROR
Enter the time in which car stopped :20
Final velocity=0 m/s
time taken to stop car is 20.0 s
distance covred=20m
Initial velocity= 2.0 m/s
Acceleration is : -0.2 m/s^2

'''



'''
Problem statement 4: Find the area of plots to build housing society 
take input from user in length and breadth of the site in Meter
and area is in meter square.
'''
print("Good Morning Sir!!!\nLets see the area of plots we bought to build the Stark Tower")
print("\nKindly enter the length and breadth of the plot in meter to avoid output in other mensuration unts")

length=float(input("Enter the length of the plot :"))
brdth=float(input("Enter the breadth of the plot :"))
area=length*brdth

print("Area of the plot of entered is",area,"m/s^2")

'''
OUTPUT OF PROBLEM STATEMENT 4:
Good Morning Sir!!!
Lets see the area of plots we bought to build the Stark Tower

Kindly enter the length and breadth of the plot in meter to avoid output in other mensuration unts
Enter the length of the plot :22
Enter the breadth of the plot :1.5
Area of the plot of entered is 33.0 m/s^2

'''


# In[ ]:




