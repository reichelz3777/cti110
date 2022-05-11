# CTI-110
# P3HW2 - Pizza Order
# Zachary Reichel 
# 4/2/22
#
#Ask user for number of students.
#Ask for number of people per pizza.
#Evaluate if number is valid
#Calculate number of pizza and rounds
#Calculates amount to be paid
#Prints receipt for user

import math

numStudents = int(input('How many students do you want to order pizza for? '))
peoplePizza = float(input('Enter number of people per pizza ( 1.5, 2 or 3): '))

if peoplePizza == 1.5 or peoplePizza == 2 or peoplePizza == 3:
    numPizzas = math.ceil(numStudents / peoplePizza)
    total = numPizzas * 5
    total = total + (total * 0.06)
    print('\n')
    print ("----Pizza Order--------") 
    print ("Number of students : ",numStudents)
    print ("Pizzas Needed : ",numPizzas)
    print (f'Price ${total:.2f}')
    print ("-------------------------------")
else:
    print ("""INVALID ENTRY!!!!
Should have entered 1.5, 2  or 3\n""")
    print("Run program again")


