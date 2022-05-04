#!/usr/bin/env python
# coding: utf-8

# In[24]:


"""
Name:Abhijeet Sharnagat
Roll no: 642
Problem: 1. Write a Python program for following conditions.

 If n is single digit print square of it.

 If n is two digit print square root of it.

 If n is three digit print cube root of it."""

#Input-

n=int(input("Enter the number:")) #Asking the user to enter the number

if n>0 and n<10: #Condition when input is 1 digit number
    square=n*n
    print("The square is",square)
elif n>9 and n<100: #Condition when input is 2 digit number
    squareroot=n**.5
    print("The square root is",squareroot)
elif n>99 and n<1000: #Condition when input is 3 digit number
    cuberoot=n**(1/3)
    print("The cuberoot is",cuberoot)
else: #Condotion when input is negative or more than three digit number
    print("Enter one,two or three digit number") 

#Output
#Enter the number:125
#The cuberoot is 5.0


# In[33]:


#Problem2: If the three sides of the triangle are entered ,write a program to check weather the triangle is equilateral or not.

#Input
s1=int(input("Enter first side:"))#Taking input of length 1st side
s2=int(input("Enter second side:")) #Taking input of length 2nd side
s3=int(input("Enter third side:")) #Taking input of length 3rd side
if s1==s2 and s1==s3:  #Condition when all sides are equal
    print("The triangle is equilateral triangle")
else:            #Condition when all sides are not equal
    print("The triangle is not equilateral")
    
"""
Output:
Enter first side:12
Enter second side:12
Enter third side:12
The triangle is equilateral triangle

"""

