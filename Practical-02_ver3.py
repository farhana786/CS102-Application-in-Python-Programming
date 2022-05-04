#Name : Veeraj Goudar
#Roll no : 624
#Problem Statement 1 :Write a Python program for following conditions.
                     # If n is single digit print square of it.
                     # If n is two digit print square root of it.
                     # If n is three digit print cube root of it.

try:                                                                        #Try allows us to test a block for error and provides the output for the block
    num=int(input('Enter a number between 1 and 1000: '))
    if num>0 and num<10:                                                    #Nested if else used for multiple case 
        print(f'The {num} is single digit so its square','is',num**2,'\n')       #Squaring the numbers for single digit numbers

    elif num>10 and num<100:                                                #Logical and operator used
        num2=num**.5                                                        #reverting the 2 digit number to its square root
        print(f'The {num} is double digit so its square root','is',f'{num2:.2f}','\n')       #using formatted strings

    elif num>100 and num<1000:
        num2= num**.3333333333333333                                        #Reverting the 3 digit number into its cube root
        print(f'The {num} is double digit so its cube root','is',f'{num2:.2f}','\n')

    else :
        print('\nThe entered value is exceeding the limit','\n')                 #If the user enters number which exceeds limit

except ValueError:                                                          #Except allows us to correct the error
    print('Enter a Natural number !!!','\n')                                     #If user enters a number except natural number


#Problem Statement 2: If Aman is playing a game which has 3 levels if Aman surpasses level 1 give him reward of 1000 coins and if clears level 2 reward
#  him with 2000 coins and if clears level 3 reward him with 3000 coins if he fails any level tell him to try again 
# (*Rewarding and providing restart can be just print statemnts*) (Surpassing of level can be done by defeating each level character consider level 1 character as
#  A level 2 character as B level 3 character as C)

print("Welcome to the Quiz Game")

print("Level 1")

#print("Boss1: What is the capital of India ")
answer=input("Boss 1: What is the capital of India ")       #input for the answer of question

if (answer == 'Delhi' or answer == 'delhi'):                #if statement with logical or operator
    print("Correct Answer you defeated Boss 1")
    coins=1000
    print(f"You've recieved {coins} for defeating Boss 1",'\n')     #Using formatted string

else:                                                       #If if condition is not true
    print("Incorrect Answer!!!!!! Try again")       
    answer=input("Boss 1: What is the capital of India ")

    if (answer == 'Delhi' or answer == 'delhi' or answer=='DELHI'):            #using if again for second try
        print("Correct Answer you defeated Boss 1")
        coins=1000
        print(f"You've recieved {coins} for defeating Boss 1",'\n')
    
    else:
        print("Incorrect Answer Again you Failed Level 1 Retry Again")
        coins=0
        exit(1)                                         #Exit the program if the user gives the incorrect value twice

try:
    answer2=int(input("Boss 2: What is 4*4*2*1 :"))
    if (answer2 == 32):
        print("Correct Answer you defeated Boss 2")
        coins=coins+2000
        print(f"You've recieved 2000 coins for defeating Boss 2 total coins now is {coins} coins",'\n')

    else:
        print("Incorrect Answer!!!!!! Try again")
        answer2=int(input("Boss 2: What is 4*4*2*1 :"))
        if (answer2 == 32):
            print("Correct Answer you defeated Boss 2")
            coins=coins+2000                            #Increment of the coins for entering correct value
            print(f"You've recieved 2000 coins for defeating Boss 2 total coins now is {coins} coins",'\n')
                
        else:
            print("Incorrect Answer Again you Failed Level 2 ")
            exit(1)

except ValueError:
    print("Enter the correct integer value")

try:
    answer3=int(input("Boss 3: What is the value of x in 2x+8=10"))
    if (answer3 == 1):
        print("Correct Answer you defeated Boss 3")
        coins=coins+3000
        print(f"You've recieved 3000 coins for defeating Boss 3 total coins now is {coins} coins",'\n')
        print("You've Completed the game congratulations")

    else:
        print("Incorrect Answer!!!!!! Try again")
        answer3=int(input("Boss 3: What is the value of x in 2x+8=10"))
        if (answer3 == 1):
            print("Correct Answer you defeated Boss 3")
            coins=coins+3000
            print(f"You've recieved 3000 coins for defeating Boss 3 total coins now is {coins} coins",'\n')
            print("You've Completed the game congratulations",'\n','\n')
                
        else:
            print("Incorrect Answer Again you Failed Level 3")
            exit(1)

except ValueError:
    print("Enter the correct integer value")

#3.  A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student allowed to sit in exam or not.

classes_held = int(input("Enter the number of classes conducted: "))            #input for no of classes
name_stud = input("Enter the name of the student: ")                            #input for name of the student
classes_attended = int(input(f"Enter the number of classes attended by {name_stud}: "))   #Attended by the student

percentage_stud = (classes_attended*100)/classes_held           #converting the attendance into percentage

if(percentage_stud>=75):                                        #If above 75% attendance is attained by student
    print(f"The student : {name_stud} has attendance of{percentage_stud}% and is allowed to sit in exam !!")

else:
    print(f"The student: {name_stud} has attendance of {percentage_stud}% and it is below 75% so student is not allowed to sit in the exam!!",'\n','\n')


#4. Check whether the triangle is equilateral, scalene, or isosceles

triside = int(input("Enter the number of sides equal in the traingle: "))

if(triside==1):                                 #If none of the is equal it is considered as scalene triangle
    print("The given triangle is a scalene triangle with none of the side is equal!!!")

elif(triside==2):                               #If two sides of the triangle are equal then its isosceles triangle
    print("The given triangle is an isosceles triangle with two sides being equal!!!")

elif(triside==3):                               #If all the sides of the triangle are equal then its considered as equilateral triangle    
    print("The given triangle is an equilateral triangle with all the side being equal!!!")

else:
    print("The triangle has only three sides please enter the correct value")


# OUTPUT


# Enter a number between 1 and 1000: 256
# The 256 is double digit so its cube root is 6.35 

# Welcome to the Quiz Game
# Level 1
# Boss 1: What is the capital of India Pune
# Incorrect Answer!!!!!! Try again
# Boss 1: What is the capital of India Delhi
# Correct Answer you defeated Boss 1
# You've recieved 1000 for defeating Boss 1

# Boss 2: What is 4*4*2*1 :32
# Correct Answer you defeated Boss 2
# You've recieved 2000 coins for defeating Boss 2 total coins now is 3000 coins

# Boss 3: What is the value of x in 2x+8=101
# Correct Answer you defeated Boss 3
# You've recieved 3000 coins for defeating Boss 3 total coins now is 6000 coins

# You've Completed the game congratulations
# Enter the number of classes conducted: 100
# Enter the name of the student: Sumit
# Enter the number of classes attended by Sumit: 79
# The student : Sumit has attendance of79.0% and is allowed to sit in exam !!
# Enter the number of sides equal in the traingle: 2
# The given triangle is an isosceles triangle with two sides being equal!!!