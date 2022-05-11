# CTI-110
# P4HW2 - Pizza Order
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

def main():
    numStudents = int(input('How many students do you want to order pizza for? '))
    peoplePizza = float(input('Enter number of people per pizza ( 1.5, 2 or 3): '))
    while not (peoplePizza == float(1.5) or peoplePizza == float(2) or peoplePizza == float(3)):
        print()
        print ("""INVALID ENTRY!!!!
Should have entered 1.5, 2  or 3\n""")
        print()
        peoplePizza = float(input('Enter number of people per pizza again. ( 1.5, 2 or 3): '))
        
    numSlices = numStudents * 3
    numPizzas = numStudents / peoplePizza
    numPizzas = math.ceil(numPizzas)
    total = (numPizzas * 5)
    tax = total * 0.06
    total = total + tax
        
    print ("----PIZZA ORDER--------") 
    print ("Number of students : ",numStudents)
    print ("Pizzas Needed : ",numPizzas)
    print (f'Price ${total:.2f}')
    print ("-------------------------------")
    while True:
        choice = input("Would you like to run the program again? ")
        if choice not in ('y', 'n'):
            print("Invalid. Try again.")
            break
        if choice == 'y':
            main()
        else:
            print("Goodbye")
            break

main()
    
